from utils.csv_loader import load_csv_data
from utils.query_function import process_data_query
from core.config import ORG_COLUMN

def get_columns_for_org(organization_name: str) -> list:
    return ORG_COLUMN.get(organization_name, ORG_COLUMN["__default__"])

def search_employee(
    query,
    filters,
    organization_name,
    page,
    page_size,
    search_fields,
    filter_fileds,
    csv_path
):
    data = load_csv_data(csv_path)
    
    parsed_filters = {key: filters.get(key) for key in filter_fileds if filters.get(key) is not None}
    
    return_fields = get_columns_for_org(organization_name)
    
    return process_data_query(
        data=data,
        query=query,
        search_fields=search_fields,
        filters=parsed_filters,
        return_fields=return_fields,
        page=page,
        page_size=page_size
    )
    

    