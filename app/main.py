from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Moi Miten menee!", "v": "0.1" }


@app.get("/hello")
def read_hello():
    return {"msg": "Hello, World!"}




@app.get("/api/ip")
async def read_root(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}