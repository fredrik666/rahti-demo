from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

rooms = [
    {"room_number": 101, "type": "single", "price": 100},
    {"room_number": 202, "type": "double", "price": 150},
    {"room_number": 303, "type": "suite", "price": 200}
]
@app.get("/")
def read_root():
    return {"msg": "Welcome to the Hotel API!"}

@app.get("/rooms")
def get_rooms():
    return {"rooms": rooms}