# Backend Development Guide

## 🎯 Overview

The Food Market Platform backend is built with **FastAPI**, **MongoDB**, and **Python**, providing a robust, scalable, and accessible API for the platform.

### Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **MongoDB** - NoSQL database for flexible data storage
- **Pydantic** - Data validation and settings management
- **Motor** - Async MongoDB driver
- **JWT** - JSON Web Tokens for authentication
- **Pytest** - Testing framework
- **Docker** - Containerization
- **Redis** - Caching layer

---

## 🏗️ Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py              # Configuration management
│   ├── dependencies.py        # Dependency injection
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── auth.py           # Authentication middleware
│   │   ├── cors.py           # CORS configuration
│   │   ├── rate_limit.py     # Rate limiting
│   │   ├── logging.py        # Request logging
│   │   └── error_handler.py  # Global error handling
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py           # User data models
│   │   ├── market.py         # Market data models
│   │   ├── product.py        # Product data models
│   │   ├── order.py          # Order data models
│   │   └── statistics.py     # Statistics models
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py   # User business logic
│   │   ├── market_service.py # Market business logic
│   │   ├── product_service.py # Product business logic
│   │   ├── order_service.py  # Order business logic
│   │   ├── analytics_service.py # Analytics logic
│   │   └── email_service.py  # Email notifications
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py           # API dependencies
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py      # User endpoints
│   │       ├── markets.py    # Market endpoints
│   │       ├── products.py   # Product endpoints
│   │       ├── orders.py     # Order endpoints
│   │       └── analytics.py  # Analytics endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py       # Security utilities
│   │   ├── database.py       # Database connection
│   │   ├── config.py         # Core configuration
│   │   └── exceptions.py     # Custom exceptions
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py     # Custom validators
│   │   ├── helpers.py        # Utility functions
│   │   ├── constants.py      # Application constants
│   │   └── pagination.py     # Pagination utilities
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py       # Test configuration
│       ├── test_users.py     # User tests
│       ├── test_markets.py   # Market tests
│       ├── test_products.py  # Product tests
│       └── test_orders.py    # Order tests
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── .env.example
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python** 3.11+
- **MongoDB** 6.0+
- **Redis** 7.0+
- **Docker** and **Docker Compose**

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/food-market.git
cd food-market/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start MongoDB and Redis (using Docker)
docker-compose up -d mongodb redis

# Run the application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Development Commands

```bash
# Start development server
uvicorn app.main:app --reload

# Run tests
pytest

# Run tests with coverage
pytest --cov=app --cov-report=html

# Run linting
flake8 app/
black app/
isort app/

# Run type checking
mypy app/

# Start all services with Docker
docker-compose up -d

# Stop all services
docker-compose down
```

---

## ⚙️ Configuration

### Environment Variables

```bash
# .env
# Database
MONGODB_URL=mongodb://localhost:27017/food_market
REDIS_URL=redis://localhost:6379

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# External Services
CLERK_SECRET_KEY=your-clerk-secret-key
EMAIL_SERVICE_URL=smtp://localhost:1025

# Application
DEBUG=True
ENVIRONMENT=development
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# Rate Limiting
RATE_LIMIT_PER_MINUTE=100
RATE_LIMIT_PER_HOUR=1000
```

### Configuration Management

```python
# app/config.py
from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # Database
    mongodb_url: str = "mongodb://localhost:27017/food_market"
    redis_url: str = "redis://localhost:6379"
    
    # Security
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # External Services
    clerk_secret_key: str
    email_service_url: str = "smtp://localhost:1025"
    
    # Application
    debug: bool = False
    environment: str = "production"
    cors_origins: List[str] = []
    
    # Rate Limiting
    rate_limit_per_minute: int = 100
    rate_limit_per_hour: int = 1000
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

---

## 🗄️ Database Setup

### MongoDB Connection

```python
# app/core/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings
import logging

logger = logging.getLogger(__name__)

class Database:
    client: AsyncIOMotorClient = None
    db = None

db = Database()

async def connect_to_mongo():
    """Create database connection."""
    try:
        db.client = AsyncIOMotorClient(settings.mongodb_url)
        db.db = db.client.get_default_database()
        logger.info("Connected to MongoDB")
    except Exception as e:
        logger.error(f"Could not connect to MongoDB: {e}")
        raise

async def close_mongo_connection():
    """Close database connection."""
    if db.client:
        db.client.close()
        logger.info("Disconnected from MongoDB")

def get_database():
    """Get database instance."""
    return db.db
```

### Redis Connection

```python
# app/core/cache.py
import redis.asyncio as redis
from app.config import settings
import logging

logger = logging.getLogger(__name__)

class RedisCache:
    def __init__(self):
        self.redis_client = None

    async def connect(self):
        """Connect to Redis."""
        try:
            self.redis_client = redis.from_url(settings.redis_url)
            await self.redis_client.ping()
            logger.info("Connected to Redis")
        except Exception as e:
            logger.error(f"Could not connect to Redis: {e}")
            raise

    async def disconnect(self):
        """Disconnect from Redis."""
        if self.redis_client:
            await self.redis_client.close()
            logger.info("Disconnected from Redis")

    async def get(self, key: str):
        """Get value from cache."""
        if self.redis_client:
            return await self.redis_client.get(key)
        return None

    async def set(self, key: str, value: str, expire: int = 3600):
        """Set value in cache."""
        if self.redis_client:
            await self.redis_client.set(key, value, ex=expire)

    async def delete(self, key: str):
        """Delete value from cache."""
        if self.redis_client:
            await self.redis_client.delete(key)

cache = RedisCache()
```

---

## 🔐 Authentication & Authorization

### JWT Authentication

```python
# app/core/security.py
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generate password hash."""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt

def verify_token(token: str) -> Optional[dict]:
    """Verify JWT token."""
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except JWTError:
        return None
```

### Authentication Middleware

```python
# app/middleware/auth.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import verify_token
from app.services.user_service import UserService
from app.models.user import UserPublic

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_service: UserService = Depends()
) -> UserPublic:
    """Get current authenticated user."""
    token = credentials.credentials
    payload = verify_token(token)
    
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = await user_service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user

async def get_current_active_user(
    current_user: UserPublic = Depends(get_current_user)
) -> UserPublic:
    """Get current active user."""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user

def require_role(required_role: str):
    """Require specific user role."""
    def role_checker(current_user: UserPublic = Depends(get_current_active_user)):
        if current_user.role != required_role and current_user.role != "super_admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        return current_user
    return role_checker
```

---

## 📊 Data Models

### Base Model

```python
# app/models/base.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class BaseDBModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
```

### User Model

```python
# app/models/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional, Dict, Any
from datetime import datetime
from .base import BaseDBModel, PyObjectId

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., max_length=100)
    role: Literal["customer", "market_admin", "super_admin"] = "customer"
    locale: Literal["en", "ua"] = "en"
    phone: Optional[str] = None
    address: Optional[str] = None
    preferences: Dict[str, Any] = Field(default_factory=dict)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
    confirm_password: str

class UserInDB(UserBase, BaseDBModel):
    hashed_password: str
    is_active: bool = True
    email_verified: bool = False
    last_login: Optional[datetime] = None

class UserPublic(UserBase):
    id: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True
```

### Market Model

```python
# app/models/market.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
from .base import BaseDBModel, PyObjectId

class MarketBase(BaseModel):
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    contact_email: EmailStr
    contact_phone: Optional[str] = None
    address: str
    coordinates: Optional[Dict[str, float]] = None
    business_hours: Dict[str, Any] = Field(default_factory=dict)
    delivery_options: List[str] = ["pickup"]
    payment_methods: List[str] = ["cash", "card"]
    is_active: bool = True

class MarketCreate(MarketBase):
    owner_id: str

class MarketInDB(MarketBase, BaseDBModel):
    owner_id: str
    verified: bool = False
    rating: float = 0.0
    total_orders: int = 0
    total_revenue: float = 0.0

class MarketPublic(MarketBase):
    id: str
    owner_id: str
    created_at: datetime
    verified: bool
    rating: float
    total_orders: int
    total_revenue: float

    class Config:
        from_attributes = True
```

---

## 🔧 Services Layer

### Base Service

```python
# app/services/base_service.py
from typing import List, Optional, TypeVar, Generic, Type
from motor.motor_asyncio import AsyncIOMotorCollection
from app.core.database import get_database
from app.models.base import BaseDBModel

ModelType = TypeVar("ModelType", bound=BaseDBModel)

class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], collection_name: str):
        self.model = model
        self.collection: AsyncIOMotorCollection = get_database()[collection_name]

    async def create(self, obj_in: dict) -> ModelType:
        """Create a new document."""
        obj_data = obj_in.copy()
        result = await self.collection.insert_one(obj_data)
        obj_data["_id"] = result.inserted_id
        return self.model(**obj_data)

    async def get_by_id(self, id: str) -> Optional[ModelType]:
        """Get document by ID."""
        from bson import ObjectId
        obj = await self.collection.find_one({"_id": ObjectId(id)})
        return self.model(**obj) if obj else None

    async def get_many(
        self,
        skip: int = 0,
        limit: int = 100,
        filter_dict: dict = None
    ) -> List[ModelType]:
        """Get multiple documents."""
        filter_dict = filter_dict or {}
        cursor = self.collection.find(filter_dict).skip(skip).limit(limit)
        documents = await cursor.to_list(length=limit)
        return [self.model(**doc) for doc in documents]

    async def update(self, id: str, obj_in: dict) -> Optional[ModelType]:
        """Update document."""
        from bson import ObjectId
        obj_in["updated_at"] = datetime.utcnow()
        result = await self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": obj_in}
        )
        if result.modified_count:
            return await self.get_by_id(id)
        return None

    async def delete(self, id: str) -> bool:
        """Delete document."""
        from bson import ObjectId
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
```

### User Service

```python
# app/services/user_service.py
from typing import Optional
from app.services.base_service import BaseService
from app.models.user import UserInDB, UserCreate, UserPublic
from app.core.security import get_password_hash, verify_password
from datetime import datetime

class UserService(BaseService[UserInDB]):
    def __init__(self):
        super().__init__(UserInDB, "users")

    async def create_user(self, user_create: UserCreate) -> UserPublic:
        """Create a new user."""
        if user_create.password != user_create.confirm_password:
            raise ValueError("Passwords do not match")
        
        # Check if user already exists
        existing_user = await self.get_by_email(user_create.email)
        if existing_user:
            raise ValueError("User with this email already exists")
        
        # Create user document
        user_data = user_create.dict(exclude={"password", "confirm_password"})
        user_data["hashed_password"] = get_password_hash(user_create.password)
        
        user = await self.create(user_data)
        return UserPublic(**user.dict())

    async def get_by_email(self, email: str) -> Optional[UserInDB]:
        """Get user by email."""
        user = await self.collection.find_one({"email": email})
        return UserInDB(**user) if user else None

    async def authenticate_user(self, email: str, password: str) -> Optional[UserInDB]:
        """Authenticate user with email and password."""
        user = await self.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def update_last_login(self, user_id: str):
        """Update user's last login time."""
        await self.collection.update_one(
            {"_id": user_id},
            {"$set": {"last_login": datetime.utcnow()}}
        )

    async def update_preferences(self, user_id: str, preferences: dict) -> Optional[UserPublic]:
        """Update user preferences."""
        user = await self.update(user_id, {"preferences": preferences})
        return UserPublic(**user.dict()) if user else None
```

### Market Service

```python
# app/services/market_service.py
from typing import List, Optional
from app.services.base_service import BaseService
from app.models.market import MarketInDB, MarketCreate, MarketPublic
from app.core.database import get_database

class MarketService(BaseService[MarketInDB]):
    def __init__(self):
        super().__init__(MarketInDB, "markets")

    async def create_market(self, market_create: MarketCreate) -> MarketPublic:
        """Create a new market."""
        # Check if user already owns a market
        existing_market = await self.get_by_owner(market_create.owner_id)
        if existing_market:
            raise ValueError("User already owns a market")
        
        market = await self.create(market_create.dict())
        return MarketPublic(**market.dict())

    async def get_by_owner(self, owner_id: str) -> Optional[MarketInDB]:
        """Get market by owner ID."""
        market = await self.collection.find_one({"owner_id": owner_id})
        return MarketInDB(**market) if market else None

    async def get_active_markets(self, skip: int = 0, limit: int = 100) -> List[MarketPublic]:
        """Get all active markets."""
        markets = await self.get_many(skip, limit, {"is_active": True})
        return [MarketPublic(**market.dict()) for market in markets]

    async def search_markets(self, query: str, skip: int = 0, limit: int = 100) -> List[MarketPublic]:
        """Search markets by name or description."""
        filter_dict = {
            "is_active": True,
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"description": {"$regex": query, "$options": "i"}}
            ]
        }
        markets = await self.get_many(skip, limit, filter_dict)
        return [MarketPublic(**market.dict()) for market in markets]

    async def update_market_stats(self, market_id: str, order_amount: float):
        """Update market statistics."""
        await self.collection.update_one(
            {"_id": market_id},
            {
                "$inc": {
                    "total_orders": 1,
                    "total_revenue": order_amount
                }
            }
        )
```

---

## 🌐 API Endpoints

### Main Application

```python
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import connect_to_mongo, close_mongo_connection
from app.core.cache import cache
from app.middleware.error_handler import add_error_handlers
from app.api.v1 import users, markets, products, orders, analytics
from app.config import settings

app = FastAPI(
    title="Food Market Platform API",
    description="API for Food Market Platform",
    version="1.0.0",
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Event handlers
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()
    await cache.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()
    await cache.disconnect()

# Add error handlers
add_error_handlers(app)

# Include routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(markets.router, prefix="/api/v1/markets", tags=["markets"])
app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["orders"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])
```

### User Endpoints

```python
# app/api/v1/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.models.user import UserCreate, UserPublic
from app.services.user_service import UserService
from app.middleware.auth import get_current_active_user, require_role
from app.core.security import create_access_token
from datetime import timedelta
from app.config import settings

router = APIRouter()

@router.post("/register", response_model=UserPublic)
async def register(
    user_create: UserCreate,
    user_service: UserService = Depends()
):
    """Register a new user."""
    try:
        user = await user_service.create_user(user_create)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/login")
async def login(
    email: str,
    password: str,
    user_service: UserService = Depends()
):
    """Login user and return access token."""
    user = await user_service.authenticate_user(email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Update last login
    await user_service.update_last_login(str(user.id))
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": settings.access_token_expire_minutes * 60,
        "user": UserPublic(**user.dict())
    }

@router.get("/me", response_model=UserPublic)
async def get_current_user_info(
    current_user: UserPublic = Depends(get_current_active_user)
):
    """Get current user information."""
    return current_user

@router.put("/me", response_model=UserPublic)
async def update_current_user(
    user_update: dict,
    current_user: UserPublic = Depends(get_current_active_user),
    user_service: UserService = Depends()
):
    """Update current user information."""
    user = await user_service.update(str(current_user.id), user_update)
    return UserPublic(**user.dict()) if user else current_user
```

### Market Endpoints

```python
# app/api/v1/markets.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from app.models.market import MarketCreate, MarketPublic
from app.services.market_service import MarketService
from app.middleware.auth import get_current_active_user, require_role
from app.utils.pagination import PaginationParams, paginate

router = APIRouter()

@router.get("/", response_model=List[MarketPublic])
async def get_markets(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    verified: Optional[bool] = None,
    search: Optional[str] = None,
    market_service: MarketService = Depends()
):
    """Get list of markets."""
    filter_dict = {"is_active": True}
    
    if verified is not None:
        filter_dict["verified"] = verified
    
    if search:
        markets = await market_service.search_markets(search, skip, limit)
    else:
        markets = await market_service.get_many(skip, limit, filter_dict)
        markets = [MarketPublic(**market.dict()) for market in markets]
    
    return markets

@router.get("/{market_id}", response_model=MarketPublic)
async def get_market(
    market_id: str,
    market_service: MarketService = Depends()
):
    """Get specific market details."""
    market = await market_service.get_by_id(market_id)
    if not market:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Market not found"
        )
    return MarketPublic(**market.dict())

@router.post("/", response_model=MarketPublic)
async def create_market(
    market_create: MarketCreate,
    current_user = Depends(require_role("market_admin")),
    market_service: MarketService = Depends()
):
    """Create a new market."""
    try:
        market = await market_service.create_market(market_create)
        return market
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{market_id}", response_model=MarketPublic)
async def update_market(
    market_id: str,
    market_update: dict,
    current_user = Depends(require_role("market_admin")),
    market_service: MarketService = Depends()
):
    """Update market details."""
    market = await market_service.update(market_id, market_update)
    if not market:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Market not found"
        )
    return MarketPublic(**market.dict())
```

---

## 🧪 Testing

### Test Configuration

```python
# app/tests/conftest.py
import pytest
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.main import app
from app.core.database import get_database
from app.services.user_service import UserService
from app.models.user import UserCreate

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def test_db():
    """Create test database."""
    client = AsyncIOMotorClient("mongodb://localhost:27017/test_food_market")
    db = client.test_food_market
    yield db
    await client.drop_database("test_food_market")
    client.close()

@pytest.fixture
async def client(test_db):
    """Create test client."""
    app.dependency_overrides[get_database] = lambda: test_db
    async with app.test_client() as client:
        yield client
    app.dependency_overrides.clear()

@pytest.fixture
async def user_service(test_db):
    """Create user service instance."""
    return UserService()

@pytest.fixture
async def test_user(user_service):
    """Create test user."""
    user_data = UserCreate(
        email="test@example.com",
        name="Test User",
        password="testpassword123",
        confirm_password="testpassword123",
        role="customer"
    )
    user = await user_service.create_user(user_data)
    return user
```

### User Tests

```python
# app/tests/test_users.py
import pytest
from httpx import AsyncClient
from app.main import app
from app.services.user_service import UserService

@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    """Test user registration."""
    user_data = {
        "email": "newuser@example.com",
        "name": "New User",
        "password": "password123",
        "confirm_password": "password123",
        "role": "customer"
    }
    
    response = await client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["name"] == user_data["name"]
    assert "id" in data

@pytest.mark.asyncio
async def test_login_user(client: AsyncClient, test_user):
    """Test user login."""
    login_data = {
        "email": "test@example.com",
        "password": "testpassword123"
    }
    
    response = await client.post("/api/v1/users/login", json=login_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert "user" in data

@pytest.mark.asyncio
async def test_get_current_user(client: AsyncClient, test_user):
    """Test getting current user info."""
    # First login to get token
    login_response = await client.post("/api/v1/users/login", json={
        "email": "test@example.com",
        "password": "testpassword123"
    })
    token = login_response.json()["access_token"]
    
    # Get current user
    response = await client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    
    data = response.json()
    assert data["email"] == test_user.email
    assert data["name"] == test_user.name
```

### Market Tests

```python
# app/tests/test_markets.py
import pytest
from httpx import AsyncClient
from app.services.market_service import MarketService

@pytest.mark.asyncio
async def test_get_markets(client: AsyncClient):
    """Test getting list of markets."""
    response = await client.get("/api/v1/markets/")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.asyncio
async def test_create_market(client: AsyncClient, test_user):
    """Test creating a new market."""
    # First login as market admin
    login_response = await client.post("/api/v1/users/login", json={
        "email": "test@example.com",
        "password": "testpassword123"
    })
    token = login_response.json()["access_token"]
    
    market_data = {
        "name": "Test Market",
        "description": "A test market",
        "contact_email": "market@example.com",
        "address": "123 Test St",
        "owner_id": str(test_user.id)
    }
    
    response = await client.post(
        "/api/v1/markets/",
        json=market_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    
    data = response.json()
    assert data["name"] == market_data["name"]
    assert data["contact_email"] == market_data["contact_email"]
```

---

## 🔧 Middleware

### Error Handling

```python
# app/middleware/error_handler.py
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
import logging

logger = logging.getLogger(__name__)

def add_error_handlers(app: FastAPI):
    """Add global error handlers."""
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """Handle validation errors."""
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "error": {
                    "code": "VALIDATION_ERROR",
                    "message": "Validation failed",
                    "details": exc.errors()
                }
            }
        )
    
    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        """Handle value errors."""
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error": {
                    "code": "VALUE_ERROR",
                    "message": str(exc)
                }
            }
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """Handle general exceptions."""
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": {
                    "code": "INTERNAL_ERROR",
                    "message": "An internal server error occurred"
                }
            }
        )
```

### Rate Limiting

```python
# app/middleware/rate_limit.py
from fastapi import Request, HTTPException, status
from app.core.cache import cache
import time
import json

class RateLimiter:
    def __init__(self, requests_per_minute: int = 100):
        self.requests_per_minute = requests_per_minute
    
    async def check_rate_limit(self, request: Request):
        """Check if request is within rate limit."""
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"
        
        # Get current requests count
        current_requests = await cache.get(key)
        if current_requests is None:
            current_requests = 0
        else:
            current_requests = int(current_requests)
        
        # Check if limit exceeded
        if current_requests >= self.requests_per_minute:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded"
            )
        
        # Increment request count
        await cache.set(key, str(current_requests + 1), expire=60)

rate_limiter = RateLimiter()

async def rate_limit_middleware(request: Request, call_next):
    """Rate limiting middleware."""
    await rate_limiter.check_rate_limit(request)
    response = await call_next(request)
    return response
```

---

## 🚀 Deployment

### Docker Configuration

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app
RUN chown -R app:app /app
USER app

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MONGODB_URL=mongodb://mongodb:27017/food_market
      - REDIS_URL=redis://redis:6379
      - DEBUG=False
    depends_on:
      - mongodb
      - redis
    volumes:
      - ./logs:/app/logs

  mongodb:
    image: mongo:6.0
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=password
    volumes:
      - mongodb_data:/data/db

  redis:
    image: redis:7.0-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  mongodb_data:
  redis_data:
```

### Production Configuration

```python
# app/core/config.py
import os
from pydantic_settings import BaseSettings

class ProductionSettings(BaseSettings):
    # Database
    mongodb_url: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017/food_market")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Security
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Application
    debug: bool = False
    environment: str = "production"
    cors_origins: list = []
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "/app/logs/app.log"
    
    class Config:
        env_file = ".env"

settings = ProductionSettings()
``` 