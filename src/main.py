from fastapi import FastAPI
from src.api.endpoints import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def read_root() -> dict:
    """
    Welcome message.
    """
    return {"message": "Welcome to Exam Prep Summarization API!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
