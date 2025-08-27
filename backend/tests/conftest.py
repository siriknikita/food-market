import pytest
import asyncio
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from app.main import app
from app.database import connect_to_mongo, close_mongo_connection
from app.config import settings


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_db():
    """Create test database connection."""
    # Use test database
    settings.database_name = "food_market_test"
    await connect_to_mongo()
    yield
    await close_mongo_connection()


@pytest.fixture
async def client(test_db):
    """Create test client."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
async def test_user():
    """Create test user data."""
    return {
        "email": "test@example.com",
        "name": "Test User",
        "password": "testpassword123",
        "role": "customer",
        "locale": "en"
    }


@pytest.fixture
async def test_market_admin():
    """Create test market admin data."""
    return {
        "email": "admin@market.com",
        "name": "Market Admin",
        "password": "adminpassword123",
        "role": "market_admin",
        "locale": "en"
    }


@pytest.fixture
async def test_market():
    """Create test market data."""
    return {
        "name": "Test Market",
        "description": "A test market",
        "contact_email": "contact@testmarket.com",
        "contact_phone": "+1234567890",
        "address": "123 Test Street"
    }


@pytest.fixture
async def test_product():
    """Create test product data."""
    return {
        "name": "Test Product",
        "description": "A test product",
        "price": 10.99,
        "stock_quantity": 100,
        "category": "Groceries",
        "sub_category": "Fruits",
        "tags": ["organic", "fresh"],
        "images": []
    } 