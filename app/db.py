import os
import psycopg

DATABASE_URL = os.getenv("DATABASE_URL")


def get_conn():
    return psycopg.connect(DATABASE_URL, autocommit=True, row_factory=psycopg.rows.dict_row)

def create_schema():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
                
                CREATE TABLE IF NOT EXISTS rooms (
                    room_id SERIAL PRIMARY KEY,
                    room_number INT NOT NULL,
                    type VARCHAR NOT NULL,
                    price NUMERIC NOT NULL,
                    occupied BOOLEAN NOT NULL DEFAULT FALSE
                );
                    
                -- lägg till nya kolumner
                ALTER TABLE rooms ADD COLUMN IF NOT EXISTS name VARCHAR(255);
            """)