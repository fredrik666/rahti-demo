from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Moi Miten menee!", "v": "0.1" }


@app.get("/hello")
def read_hello():
    return {"msg": "Hello, World!"}


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}
