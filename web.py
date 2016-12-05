from weather import get_weather
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key = os.environ.get('FORCASTIO_API')

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	name = request.values.get('name')
	return render_template('index.html', name=name)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/weather')
def weather():
	city = request.values.get('city')
	weather = get_weather(city, api_key)
	return render_template('weather.html', city=city, weather=weather)

if __name__ == "__main__":
	app.run()