from db import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Create bands table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hometown TEXT NOT NULL
        )
    ''')

    # Create venues table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')

    # Create concerts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            band_id INTEGER,
            venue_id INTEGER,
            FOREIGN KEY(band_id) REFERENCES bands(id),
            FOREIGN KEY(venue_id) REFERENCES venues(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
