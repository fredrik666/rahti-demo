from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.db import get_conn, create_schema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#testing schema creation
@app.on_event("startup")
def startup():
    try:
        create_schema()
    except Exception as e:
        print("DB init failed:", e)

@app.get("/")
def read_root():
#testing
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT 'databasen funkar!' AS message, version();")
        db_status = cur.fetchone()
    return { "msg": "Moi Miten menee!", "v": "0.1", "db_status": db_status }


@app.get("/hello")
def read_hello():
    return {"msg": "Hello, World!"}

@app.get("/if/{term}")
def if_test(term: str):
        ret_str = "Default response"
        if (term == "hello" 
            or term == "hi" 
            or term == "Greetings"):

            ret_str = "hello to you too!"
        elif term == "hej" and 1 == 0:
            ret_str = "hej på dig"
        else:
            ret_str = f"what do u mean with {term}?"
        return {"msg": ret_str}


@app.get("/api/ip")
async def read_root(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}


@app.get("/api/rooms")
def read_rooms():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT *
            FROM rooms
            ORDER BY room_number
        """)
        rooms = cur.fetchall()
    return rooms

@app.get("/api/rooms/{room_id}")
def get_room(room_id: int):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT *
            FROM rooms
            WHERE room_id = %s
        """, (room_id,))
        room = cur.fetchone()
    if room:
        return room
    else:
        return {"msg": "Room not found"}, 404

@app.post("/bookings")
def create_booking():
    return {"msg": "Booking created successfully!"}
