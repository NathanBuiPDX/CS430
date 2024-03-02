from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from quote")
        except sqlite3.OperationalError:
            cursor.execute("create table quote (quote text, name text, date date, type text, source text, rating int)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: quote, name, date, type, source, quote's rating
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM quote")
        return cursor.fetchall()

    def insert(self, quote, name, type, source, rating):
        """
        Inserts entry into database
        :param quote: String
        :param name: String
        :param type: String
        :param source: String
        :param rating: INT
        :return: none
        :raises: Database errors on connection and insertion
        """
        params = {'quote':quote, 'name':name, 'type':type, 'date':date.today(), 'source':source, 'rating':rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into quote (quote, name, type, date, source, rating) VALUES (:quote, :name, :type, :date, :source, :rating)", params)

        connection.commit()
        cursor.close()
        return True
