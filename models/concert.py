class Concert:
    def __init__(self, conn, concert_id):
        self.conn = conn
        self.id = concert_id

        # Fetch concert data
        concert_data = self.conn.execute("SELECT * FROM concerts WHERE id = ?", (self.id,)).fetchone()
        if concert_data is None:
            raise ValueError(f"Concert with ID {self.id} does not exist.")

        self.band_id = concert_data[1]
        self.venue_id = concert_data[2]
        self.date = concert_data[3]

    def band(self):
        query = "SELECT * FROM bands WHERE id = ?"
        result = self.conn.execute(query, (self.band_id,))
        return result.fetchone()

    def venue(self):
        query = "SELECT * FROM venues WHERE id = ?"
        result = self.conn.execute(query, (self.venue_id,))
        return result.fetchone()

    def hometown_show(self):
        query = """
        SELECT concerts.* FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE bands.hometown = venues.city AND concerts.id = ?
        """
        result = self.conn.execute(query, (self.id,))
        return bool(result.fetchone())

    def introduction(self):
        query = """
        SELECT bands.name, bands.hometown, venues.city FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        """
        result = self.conn.execute(query, (self.id,))
        band_name, band_hometown, venue_city = result.fetchone()
        return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
