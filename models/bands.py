from models.concert import Concert
class Band:
    def __init__(self, conn, band_id):
        self.conn = conn
        self.id = band_id

        # Fetch band data
        band_data = self.conn.execute("SELECT * FROM bands WHERE id = ?", (self.id,)).fetchone()
        if band_data is None:
            raise ValueError(f"Band with ID {self.id} does not exist.")
        
        self.name = band_data[1]
        self.hometown = band_data[2]

    def concerts(self):
        query = "SELECT * FROM concerts WHERE band_id = ?"
        result = self.conn.execute(query, (self.id,))
        return result.fetchall()

    def venues(self):
        query = """
        SELECT DISTINCT venues.* FROM venues
        JOIN concerts ON concerts.venue_id = venues.id
        WHERE concerts.band_id = ?
        """
        result = self.conn.execute(query, (self.id,))
        return result.fetchall()

    def play_in_venue(self, venue_title, date):
        venue_query = "SELECT id FROM venues WHERE title = ?"
        venue_data = self.conn.execute(venue_query, (venue_title,)).fetchone()

        if venue_data is None:
            raise ValueError(f"Venue with title '{venue_title}' does not exist.")
        
        venue_id = venue_data[0]

        insert_query = "INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)"
        self.conn.execute(insert_query, (self.id, venue_id, date))
        self.conn.commit()

    def all_introductions(self):
        query = """
        SELECT concerts.id FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE bands.id = ?
        """
        concerts = self.conn.execute(query, (self.id,)).fetchall()
        introductions = []
        for concert in concerts:
            concert_instance = Concert(self.conn, concert_id=concert[0])
            introductions.append(concert_instance.introduction())
        return introductions

    @classmethod
    def most_performances(cls, conn):
        query = """
        SELECT bands.*, COUNT(concerts.id) AS performance_count FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        GROUP BY bands.id
        ORDER BY performance_count DESC LIMIT 1
        """
        result = conn.execute(query).fetchone()
        return result
