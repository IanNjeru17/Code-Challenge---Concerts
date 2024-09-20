import sqlite3

def get_connection():
    conn = sqlite3.connect('concerts.db')
    return conn
