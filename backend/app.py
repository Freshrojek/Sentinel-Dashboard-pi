from fastapi import FastAPI
from auth import get_access_token
from sentinel_query import query_sentinel

app = FastAPI()

@app.get("/data")
def get_data():
    token = get_access_token()
    result = query_sentinel(token)
    return result
    