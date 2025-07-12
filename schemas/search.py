from typing import List
from pydantic import BaseModel, Field

class SearchResult(BaseModel):
    total_records: int = Field(..., description="Total number of records matching the query")
    total_pages: int = Field(..., description="Total number of pages based on page size")
    page: int = Field(..., description="Current page number")
    page_size: int = Field(..., description="Number of results per page")
    data: List[dict] = Field(..., description="List of employee records")
    
    