from fastapi import FastAPI
from api.v1.api_router import router as api_router

app = FastAPI(title="CSV Search API", 
              description="A high-performance API to search employee records from a CSV file with filtering, pagination and rate limiting",
              version="1.0.0")
app.include_router(api_router, prefix="/api/v1")