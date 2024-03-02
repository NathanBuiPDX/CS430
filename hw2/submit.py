from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import quotemodel

class Submit(MethodView):
    def get(self):
        """
        Return the submit form in submit.html
        """
        return render_template('submit.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed. Enabled cancel button, which redirect to index page.
        """
        model = quotemodel.get_model()
        model.insert(request.form['quote'], request.form['name'], request.form['type'], request.form['source'], request.form['rating'])
        return redirect(url_for('index'))
