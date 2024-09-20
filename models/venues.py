class Venue:
    def __init__(self, conn, venue_id):
        self.conn = conn
        self.id = venue_id

        # Fetch venue data
        venue_data = self.conn.execute("SELECT * FROM venues WHERE id = ?", (self.id,)).fetchone()
        if venue_data is None:
            raise ValueError(f"Venue with ID {self.id} does not exist.")

        self.title = venue_data[1]
        self.city = venue_data[2]

    def concerts(self):
        query = "SELECT * FROM concerts WHERE venue_id = ?"
        result = self.conn.execute(query, (self.id,))
        return result.fetchall()

    def bands(self):
        query = """
        SELECT DISTINCT bands.* FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        """
        result = self.conn.execute(query, (self.id,))
        return result.fetchall()

    def concert_on(self, date):
        query = "SELECT * FROM concerts WHERE venue_id = ? AND date = ? LIMIT 1"
        result = self.conn.execute(query, (self.id, date))
        return result.fetchone()

    def most_frequent_band(self):
        query = """
        SELECT bands.*, COUNT(concerts.id) AS performance_count FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY performance_count DESC LIMIT 1
        """
        result = self.conn.execute(query, (self.id,))
        return result.fetchone()
