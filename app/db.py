import os
import psycopg

DATABASE_URL = os.getenv("DATABASE_URL")


def get_conn():
    return psycopg.connect(DATABASE_URL, autocommit=True, row_factory=psycopg.rows.dict_row)

def create_schema():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
                -- rooms
                CREATE TABLE IF NOT EXISTS rooms (
                    room_id SERIAL PRIMARY KEY,
                    room_number INT NOT NULL,
                    type VARCHAR NOT NULL,
                    created_at TIMESTAMP DEFAULT now(),
                    price NUMERIC NOT NULL,
                    occupied BOOLEAN NOT NULL DEFAULT FALSE
                );
                    
                -- lägg till nya kolumner
                ALTER TABLE rooms ADD COLUMN IF NOT EXISTS name VARCHAR(255);
                ALTER TABLE rooms ADD COLUMN IF NOT EXISTS price NUMERIC;
                
                -- guests
                CREATE TABLE IF NOT EXISTS guests (
                    id SERIAL PRIMARY KEY,
                    firstname VARCHAR NOT NULL,
                    lastname VARCHAR NOT NULL,
                    created_at TIMESTAMP DEFAULT now(),
                    address VARCHAR
                );
                    
                -- bookings
                CREATE TABLE IF NOT EXISTS bookings (
                    id SERIAL PRIMARY KEY,
                    guest_id INT NOT NULL,
                    room_id INT NOT NULL,
                    check_in_date DATE NOT NULL,
                    check_out_date DATE NOT NULL,
                    created_at TIMESTAMP DEFAULT now(),
                    FOREIGN KEY (guest_id) REFERENCES guests(id),
                    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
                );
                -- ADD CONSTRAINT guest_id_key FOREIGN KEY ("guest_id") REFERENCES guests(id);
                
            """)