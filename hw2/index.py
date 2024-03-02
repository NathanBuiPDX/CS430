from flask import render_template
from flask.views import MethodView
import quotemodel

class Index(MethodView):
    def get(self):
        """
        :return: the index.html page
        """
        return render_template('index.html')