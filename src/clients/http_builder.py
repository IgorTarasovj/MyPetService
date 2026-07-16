from httpx import Client

def get_http_client() -> Client:
    return Client(
        timeout=1000,
        base_url="http://127.0.0.1:8000"
    )