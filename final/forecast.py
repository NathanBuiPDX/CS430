from flask import render_template
from flask.views import MethodView
import model

class Forecast(MethodView):
    def get(self):
        """
        :return: the forecast.html page
        """
        appModel = model.get_model()
        forecastData = appModel.fetchForecastData()
        print("recived data in Index GET: ", forecastData)
        return render_template('forecast.html', forecastData=forecastData)