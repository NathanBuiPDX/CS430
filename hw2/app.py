"""
A simple guestbook flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from submit import Submit
from quote import Quote

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/quotes',
                 view_func=Quote.as_view('quotes'),
                 methods=["GET"])

app.add_url_rule('/submit',
                 view_func=Submit.as_view('submit'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
