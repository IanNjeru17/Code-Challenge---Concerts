# Code-Challenge---Concerts
**To test run the test python3 seed.py**

Deliverables

You will be writing methods that execute raw SQL queries to interact with your database. Use Python’s sqlite3 or psycopg2 library to run SQL commands.

Make sure to set up your database and tables using raw SQL commands before working on the deliverables.
Migrations

Before working on these deliverables, you need to create migrations for the concerts table. This is assuming you have already created and migrated the band and venues tables.

A Concert belongs to a Band and a Venue. In your migration, create any columns your concerts table will need to establish these relationships.

The concerts table should also have:

    A date column that stores a string.

After creating the concerts table, use raw SQL to create instances of your data so you can test your code.
Object Relationship Methods

For the following methods, write SQL queries to retrieve the necessary data from the database.

Concert

    Concert.band(): should return the Band instance for this concert.
    Concert.venue(): should return the Venue instance for this concert.

Venue

    Venue.concerts(): returns a collection of all concerts for the venue.
    Venue.bands(): returns a collection of all bands who performed at the venue.

Band

    Band.concerts(): should return a collection of all concerts the band has played.
    Band.venues(): should return a collection of all venues the band has performed at.

Aggregate and Relationship Methods

Concert

    Concert.hometown_show(): returns true if the concert is in the band's hometown, false if it is not. Use SQL joins to compare the band's hometown with the concert's venue city.
    Concert.introduction(): returns a string with the band's introduction for this concert:
        "Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"

Band

    Band.play_in_venue(venue, date): takes a venue (venue title) and date (as a string) as arguments, and creates a new concert for the band at that venue on that date. Insert the concert using raw SQL.
    Band.all_introductions(): returns an array of strings representing all the introductions for this band.
        Each introduction is in the form: "Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"
    Band.most_performances(): returns the Band that has played the most concerts. Use SQL GROUP BY and COUNT to identify the band with the most concerts.

Venue

    Venue.concert_on(date): takes a date (string) as an argument and finds the first concert on that date at the venue.
    Venue.most_frequent_band(): returns the band that has performed the most at the venue. You will need to count how many times each band has performed at this venue using a SQL GROUP BY query.
