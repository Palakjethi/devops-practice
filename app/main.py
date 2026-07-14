from fastapi import FastAPI

app = FastAPI(title="DevOps Practice App")


@app.get("/")
def read_root():
    return {"message": "Hello from inside a Docker container!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}
