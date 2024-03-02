class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

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
        pass
