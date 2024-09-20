import sqlite3
from models.bands import Band
from models.venues import Venue
from models.concert import Concert

# Open database connection
conn = sqlite3.connect('concerts.db')

# Insert sample data
conn.execute("INSERT INTO bands (name, hometown) VALUES ('Sauti Soul', 'Loitoktok')")
conn.execute("INSERT INTO venues (title, city) VALUES ('Heart the Band', 'Nairobi')")
conn.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-10-10')")
conn.commit()

# Debugging: Verify data insertion
bands = conn.execute("SELECT * FROM bands").fetchall()
venues = conn.execute("SELECT * FROM venues").fetchall()
concerts = conn.execute("SELECT * FROM concerts").fetchall()

print("Bands:", bands)  
print("Venues:", venues)  
print("Concerts:", concerts)  

# Example usage
try:
    band = Band(conn, 1)
except ValueError as e:
    print(e)

try:
    venue = Venue(conn, 1)
except ValueError as e:
    print(e)

try:
    concert = Concert(conn, 1)
except ValueError as e:
    print(e)

# Test methods 
if bands:
    print(band.concerts())  # All concerts for the band
    print(band.venues())  # All venues where the band performed
    print (f"Band Introduction :{band.all_introductions()}") 
if venues:
    print(f"All concerts at the venue:{venue.concerts()}")  
    print(f"All bands that performed at the venue:{venue.bands()}")  

if bands:
    print(Band.most_performances(conn))
conn.close()
