from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, subscription, webhook
import asyncio

app = FastAPI(
    title="SubPay Management",
    description="A subscription and payment management API with FastAPI + Stripe + PostgreSQL",
    version="1.0.0",
)

# CORS settings (allow your frontend to call the API)
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(subscription.router, prefix="/subscription", tags=["subscription"])
app.include_router(webhook.router, prefix="/webhook", tags=["webhook"])

@app.get("/", tags=["root"])
def root():
    return {"message": "SubPay API is running"}

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database tables created (if they didn't exist)")
