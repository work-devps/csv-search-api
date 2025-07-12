import os
import csv
from typing import List, Dict

_csv_cache : Dict[str, tuple] = {} 

def load_csv_data(csv_path: str) ->List[dict]:
    global _csv_cache
    
    current_modified_time = os.path.getmtime(csv_path)
    
    if csv_path not in _csv_cache or _csv_cache[csv_path][1] != current_modified_time:
        with open(csv_path, newline='',encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = []
            
            for row in reader:
                cleaned = {
                    key:value if value.strip() else f"No {key.replace('-',' ')}"
                    for key, value in row.items()
                }
                data.append(cleaned)
            _csv_cache[csv_path] = (data, current_modified_time)
            
    return _csv_cache[csv_path][0]