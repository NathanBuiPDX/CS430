from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import model

DEFAULT_CITY = "Portland"
class Index(MethodView):
    def get(self):
        """
        :return: the index.html page
        """
        appModel = model.get_model()
        data = appModel.cityData()
        print("recived data in Index GET: ", data)
        return render_template('index.html', data=data)
    
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Check if the user is making a request to change the city or changing the temperature unit
        :return: the index.html page with updated data.
        """
        appModel = model.get_model()
        data = appModel.cityData()
        if 'city' in request.form:
            city = request.form['city']
            print("city: ", city)
            data = appModel.fetchCityData(city)
        elif 'tempUnit' in request.form:
            tempUnit = request.form['tempUnit']
            print("request.form: ", tempUnit)
            data = appModel.fetchNewTempUnitData(tempUnit)
        return render_template('index.html', data=data)