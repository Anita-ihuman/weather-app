from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key (replace 'your_api_key' with your actual key)
API_KEY = '684210f7c7ae30dfd4154388aa4a6610'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form['city']

        # Make request to OpenWeatherMap API
        try:
            response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
            response.raise_for_status()
            weather_data = response.json()

            if weather_data['cod'] != 200:
                error = weather_data['message']
                weather_data = None
        except requests.exceptions.RequestException as e:
            error = str(e)

    return render_template('weather.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
