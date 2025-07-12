import time
from fastapi import Request, HTTPException

request_counters = {}

class RateLimiter:
    def __init__(self, requests_limit:int, time_window: int):
        self.requests_limit = requests_limit
        self.time_window = time_window
        
    async def __call__(self, request:Request):
        client_ip = request.client.host
        route_path = request.url.path
        current_time = int(time.monotonic())
        key = f"{client_ip}:{route_path}"

        if key not in request_counters:
            request_counters[key] = {"timestamp": current_time, "count": 1}
        else:
            entry = request_counters[key]
            if current_time - entry["timestamp"] > self.time_window:
                request_counters[key] = {"timestamp": current_time, "count": 1}
            else:
                if entry["count"] >= self.requests_limit:
                    raise HTTPException(status_code=429, detail="Rate limit exceeded.")
                request_counters[key]["count"] += 1

        for k in list(request_counters.keys()):
            if current_time - request_counters[k]["timestamp"] > self.time_window:
                request_counters.pop(k)