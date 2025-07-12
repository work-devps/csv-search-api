# CSV Search API

Fast API with high performance Fto search large CSV data with filtering, pagination and rate limit. Runs natively on CSV without the need for a database.
----

## Features
- Look for 'firstname', 'lastname', 'fullname' and 'contact'
- Group by 'status', 'position', 'department', 'company'
- Return fields that are configurable per organization
- Pagination support
- Built-in rate limiter (5 requests/minute per IP)
- Dockerized for production

----

## Project Structure
.
├── main.py
├── api/
│   └── v1/
│       ├── api_router.py
│       └── endpoints/
│           └── search.py
├── core/
│   └── config.py
├── schemas/
│   └── search.py
├── services/
│   └── search_service.py
├── utils/
│   ├── csv_loader.py
│   ├── query_function.py
│   └── rate_limiter.py
├── data/
│   └── employees.csv

---- 


## File Descriptions
| File / Folder                         | Description |
|--------------------------------------|-------------|
| `main.py`                            | Entry point that initializes the FastAPI app and includes API routers. |
| `api/v1/api_router.py`               | Groups versioned endpoints and includes the search router. |
| `api/v1/endpoints/search.py`         | Defines the `/search` GET endpoint with support for filters, query, pagination, and rate limiting. |
| `core/config.py`                     | Maps organizations to the list of returnable fields specific to that org. |
| `schemas/search.py`                  | Pydantic model for API response: includes pagination metadata and employee data. |
| `services/search_service.py`         | Core business logic: loads data, applies search/filter logic, and formats output. |
| `utils/csv_loader.py`                | Reads and caches CSV data with default placeholders for missing fields. |
| `utils/query_function.py`            | Handles filtering, searching, and paginating the records based on query params. |
| `utils/rate_limiter.py`              | Implements in-memory rate limiting by IP and route path. |
| `data/employees.csv`                 | Input data source used for the search API. |


## Quickstart

### Prerequisities

- Docker installed: https://www.docker.com/products/docker-desktop

---

### Run with Docker

```bash
# Clone the repo
git clone https://github.com/work-devps/csv-search-api.git
cd csv-search-api

# Build the image
docker build -t csv-search-api .

# Run the container
docker run -d -p 8000:8000 csv-search-api

Then open your browser:
http://localhost:8000/docs (Swagger UI)

```
### Ready to Test query examples
```bash
1. Search by query (name match)
org_name: PeopleInc
query: Nikita

✔ Returns employees named "Nikita" from PeopleInc.



2. Filter by status and department
org_name: TechCorp
status: terminated
department: Engineering

✔ Returns terminated employees in Engineering (e.g., Dinesh Kumar).



3. Search and filter by position
org_name: SellWell
query: Amit
position: Lead

✔ Returns "Amit Jain", Lead at SellWell.



4. Filter by company and status
org_name: GrowMore
company: Capgemini
status: active

✔ Returns active employees at Capgemini under GrowMore.



5. Multiple filters together
org_name: GrowMore
query: Neha
position: Executive
status: terminated

✔ Returns “Neha Verma”, a terminated Executive at GrowMore.



6. Test pagination with query
org_name: GrowMore
query: Reddy
page: 1
page_size: 2

✔ Returns page 1 of results with people whose last name is Reddy.
```