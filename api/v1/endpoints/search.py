from fastapi import APIRouter, Request, Query, Depends
from typing import Optional
from schemas.search import SearchResult
from services.search_service import search_employee
from utils.rate_limiter import RateLimiter

router = APIRouter()
rate_limiter = RateLimiter(requests_limit=5, time_window=60)

@router.get("/search", response_model=SearchResult)
async def search_csv(
    request: Request,
    org_name: str=Query(..., description="Name of the organization"),
    query: Optional[str] = Query(None, description="Search query"),
    status: Optional[str] = Query(None, description="employee status filter"),
    position: Optional[str] = Query(None, description="employee position filter"),
    department: Optional[str] = Query(None, description="employee department filter"),
    company: Optional[str] = Query(None, description="employee company filter"),
    page: int = Query(1, ge=1, description="Page number for pagination"),
    page_size: int = Query(10, le=100, description="No. of result per page"),
    allowed: bool = Depends(rate_limiter)
):
    
    """
    This API is used to search employee records from a large CSV file. Dynamically we can change which fields to used for search, filter and in which file
    """
    
    
    filters = {
        "status": status,
        "position": position,
        "department": department,
        "company":company
    }
    
    return search_employee(
        query=query,
        filters=filters,
        organization_name=org_name,
        page=page,
        page_size=page_size,
        search_fields=["firstname","lastname","contact"],
        filter_fileds=["status","position","department","company"],
        csv_path = "data/employees.csv",
    )
    