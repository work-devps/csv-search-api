def process_data_query(
    data: list,
    query: str,
    search_fields: list,
    filters: dict,
    return_fields: list,
    page: int,
    page_size: int
) -> dict:
    query = query.lower() if query else ""
    

    def matches(record):
        if not query:
            return True
        full_name = f"{record.get('firstname', '')} {record.get('lastname', '')}".lower()
        if query in full_name:
            return True
        return any(query in record.get(f, "").lower() for f in search_fields)
    
    def passes_filters(record):
        return all(record.get(key,"").lower() == value.lower() for key, value in filters.items())
    
    filtered = list(filter(lambda r: matches(r) and passes_filters(r), data))
    total_records = len(filtered)
    total_pages = (total_records + page_size-1)//page_size
    start = (page -1) * page_size
    end = start + page_size
    paginated = filtered[start:end]
    
    if return_fields:
        paginated = list(map(lambda row: {k: row.get(k) for k in return_fields}, paginated))
    
    
    return {
        "total_records":total_records,
        "total_pages": total_pages,
        "page":page,
        "page_size":page_size,
        "data":paginated
    }