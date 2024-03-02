from flask import render_template
from flask.views import MethodView
import quotemodel

class Quote(MethodView):
    def get(self):
        """
        Calls the querry to get all the rows in the database
        :return: quotes.html page with rendered quotes' details
        """
        model = quotemodel.get_model()
        entries = [dict(quote=row[0], name=row[1], date=row[2], type=row[3], source=row[4], rating=row[5] ) for row in model.select()]
        return render_template('quotes.html',entries=entries)
