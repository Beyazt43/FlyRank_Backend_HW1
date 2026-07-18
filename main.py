from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Walk the dog", "done": False},
    {"id": 3, "title": "Read a book", "done": True},
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}
