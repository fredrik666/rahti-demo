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
    {"room_id": 1, "room_number": "101", "type": "single", "price": 800, "occupied": False},
    {"room_id": 2, "room_number": "102", "type": "single", "price": 800, "occupied": True},
    {"room_id": 3, "room_number": "201", "type": "double", "price": 1200, "occupied": False},
    {"room_id": 4, "room_number": "202", "type": "double", "price": 1200, "occupied": False},
    {"room_id": 5, "room_number": "301", "type": "suite", "price": 3000, "occupied": False},
    {"room_id": 6, "room_number": "302", "type": "suite", "price": 3000, "occupied": True}
]

@app.get("/api/rooms")
def read_rooms():
    return {"rooms": rooms}