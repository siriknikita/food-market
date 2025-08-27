from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import connect_to_mongo, close_mongo_connection
from .api.v1 import auth

app = FastAPI(
    title="Food Market Platform API",
    description="A web-based food market platform with accessibility-first design",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database events
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Include routers
app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Food Market Platform API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 