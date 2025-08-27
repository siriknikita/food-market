from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from typing import Optional
from ...models.user import UserCreate, UserPublic, UserUpdate
from ...auth.jwt import get_password_hash, verify_password, create_access_token
from ...auth.dependencies import get_current_user
from ...database import get_collection
from ...config import settings
from bson import ObjectId
from datetime import datetime

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate):
    """Register a new user."""
    users_collection = get_collection("users")
    
    # Check if user already exists
    existing_user = await users_collection.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Hash password
    hashed_password = get_password_hash(user_data.password)
    
    # Create user document
    user_doc = {
        "_id": str(ObjectId()),
        "email": user_data.email,
        "name": user_data.name,
        "role": user_data.role,
        "locale": user_data.locale,
        "hashed_password": hashed_password,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    # Insert user
    await users_collection.insert_one(user_doc)
    
    # Return user without password
    return UserPublic(
        id=user_doc["_id"],
        email=user_doc["email"],
        name=user_doc["name"],
        role=user_doc["role"],
        locale=user_doc["locale"],
        created_at=user_doc["created_at"],
        updated_at=user_doc["updated_at"]
    )


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login user and return access token."""
    users_collection = get_collection("users")
    
    # Find user by email
    user_data = await users_collection.find_one({"email": form_data.username})
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verify password
    if not verify_password(form_data.password, user_data["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user_data["_id"]}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": UserPublic(
            id=user_data["_id"],
            email=user_data["email"],
            name=user_data["name"],
            role=user_data["role"],
            locale=user_data["locale"],
            created_at=user_data["created_at"],
            updated_at=user_data["updated_at"]
        )
    }


@router.get("/me", response_model=UserPublic)
async def get_current_user_info(current_user = Depends(get_current_user)):
    """Get current user information."""
    return current_user


@router.put("/me", response_model=UserPublic)
async def update_current_user(
    user_update: UserUpdate,
    current_user = Depends(get_current_user)
):
    """Update current user information."""
    users_collection = get_collection("users")
    
    # Prepare update data
    update_data = {}
    if user_update.name is not None:
        update_data["name"] = user_update.name
    if user_update.locale is not None:
        update_data["locale"] = user_update.locale
    
    if not update_data:
        return current_user
    
    update_data["updated_at"] = datetime.utcnow()
    
    # Update user
    await users_collection.update_one(
        {"_id": current_user.id},
        {"$set": update_data}
    )
    
    # Get updated user
    updated_user = await users_collection.find_one({"_id": current_user.id})
    
    return UserPublic(
        id=updated_user["_id"],
        email=updated_user["email"],
        name=updated_user["name"],
        role=updated_user["role"],
        locale=updated_user["locale"],
        created_at=updated_user["created_at"],
        updated_at=updated_user["updated_at"]
    ) 