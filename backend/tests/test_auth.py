import pytest
from httpx import AsyncClient
from app.database import get_collection
from app.auth.jwt import get_password_hash


class TestAuth:
    """Test authentication endpoints."""
    
    async def test_register_user_success(self, client: AsyncClient, test_user):
        """Test successful user registration."""
        response = await client.post("/api/v1/auth/register", json=test_user)
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == test_user["email"]
        assert data["name"] == test_user["name"]
        assert data["role"] == test_user["role"]
        assert data["locale"] == test_user["locale"]
        assert "id" in data
        assert "password" not in data
    
    async def test_register_user_duplicate_email(self, client: AsyncClient, test_user):
        """Test registration with duplicate email."""
        # First registration
        await client.post("/api/v1/auth/register", json=test_user)
        
        # Second registration with same email
        response = await client.post("/api/v1/auth/register", json=test_user)
        assert response.status_code == 400
        assert "email already registered" in response.json()["detail"].lower()
    
    async def test_register_user_invalid_password(self, client: AsyncClient, test_user):
        """Test registration with invalid password."""
        test_user["password"] = "short"
        response = await client.post("/api/v1/auth/register", json=test_user)
        assert response.status_code == 422
    
    async def test_login_success(self, client: AsyncClient, test_user):
        """Test successful login."""
        # Register user first
        await client.post("/api/v1/auth/register", json=test_user)
        
        # Login
        login_data = {
            "email": test_user["email"],
            "password": test_user["password"]
        }
        response = await client.post("/api/v1/auth/login", json=login_data)
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert "user" in data
    
    async def test_login_invalid_credentials(self, client: AsyncClient, test_user):
        """Test login with invalid credentials."""
        # Register user first
        await client.post("/api/v1/auth/register", json=test_user)
        
        # Login with wrong password
        login_data = {
            "email": test_user["email"],
            "password": "wrongpassword"
        }
        response = await client.post("/api/v1/auth/login", json=login_data)
        assert response.status_code == 401
    
    async def test_login_nonexistent_user(self, client: AsyncClient):
        """Test login with nonexistent user."""
        login_data = {
            "email": "nonexistent@example.com",
            "password": "password123"
        }
        response = await client.post("/api/v1/auth/login", json=login_data)
        assert response.status_code == 401
    
    async def test_get_current_user_success(self, client: AsyncClient, test_user):
        """Test getting current user with valid token."""
        # Register and login
        await client.post("/api/v1/auth/register", json=test_user)
        login_data = {
            "email": test_user["email"],
            "password": test_user["password"]
        }
        login_response = await client.post("/api/v1/auth/login", json=login_data)
        token = login_response.json()["access_token"]
        
        # Get current user
        headers = {"Authorization": f"Bearer {token}"}
        response = await client.get("/api/v1/auth/me", headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == test_user["email"]
    
    async def test_get_current_user_invalid_token(self, client: AsyncClient):
        """Test getting current user with invalid token."""
        headers = {"Authorization": "Bearer invalid_token"}
        response = await client.get("/api/v1/auth/me", headers=headers)
        assert response.status_code == 401
    
    async def test_get_current_user_no_token(self, client: AsyncClient):
        """Test getting current user without token."""
        response = await client.get("/api/v1/auth/me")
        assert response.status_code == 403 