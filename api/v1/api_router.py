from fastapi import APIRouter
from .endpoints import search

router = APIRouter()
router.include_router(search.router, tags=["Search"])