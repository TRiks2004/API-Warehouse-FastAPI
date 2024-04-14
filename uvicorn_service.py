from uvicorn import run
from preparation_work.app import api_factory


app = api_factory()

if __name__ == "__main__":
    run("uvicorn_service:app", host="0.0.0.0", port=8000, reload=True)
