import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def render_results():
    city = request.form['city']
    data = getWeather(city) 
    condition = data['weather'][0]['main']
    location = data["name"]
    temp = int(data['main']['temp'])
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    return render_template('results.html', location=location, condition=condition, temp=temp, wind=wind, humidity=humidity, pressure=pressure)



def getWeather(city):
    api = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ac8ee0a67ad7f025dd1b9edbc1d55bb9".format(city)
    json_data = requests.get(api).json()
    return json_data

if __name__ == '__main__':
    app.run()
