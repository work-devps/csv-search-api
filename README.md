# CSV Search API

A high performance API based on FASTAPI to search large CSV datasets with filtering, pagination and rate limiting. Runs directly on CSV without a database.
----

## Features
- Search by 'firstname', 'lastname', 'fullname' and 'contact'
- Filter by 'status', 'position', 'department', 'company'
- Configurable return fields as per organization
- Pagination support
- Built-in rate limiter (5 requests/minute per IP)
- Dockerized for production

----

## Quickstart

### Prerequisities

- Docker installed: https://www.docker.com/products/docker-desktop

---

### Run with Docker

```bash
# Clone the repo
git clone https://github.com/<your-username>/csv-search-api.git
cd csv-search-api

# Build the image
docker build -t csv-search-api .

# Run the container
docker run -d -p 8000:8000 csv-search-api

Then open your browser:
http://localhost:8000/docs (Swagger UI)

```
### Ready to Test query examples
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