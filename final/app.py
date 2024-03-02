"""
A simple guestbook flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from forecast import Forecast

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET", "POST"])

app.add_url_rule('/forecast',
                 view_func=Forecast.as_view('forecast'),
                 methods=["GET"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
