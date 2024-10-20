from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)


base = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base, "weather.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


API_KEY = "your api key"


# with this function you will save your favorite locations(model)
class FavoriteLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), unique=True, nullable=False)


# this is for  saving weather history
class WeatherHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now()) #you can add more features here


# initialize the database
with app.app_context():
    db.create_all()


# route  the homepage
@app.route("/")
def index():
    return render_template("index.html")


# route to get weather data by location
@app.route("/get_weather", methods=["POST"])
def get_weather():  # see get weather function in script file
    data = request.json
    location = data.get("location")

    # call the openweathermap API to get weather data for the location
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        #  weather data to history

        save_weather_data(location, weather_data)

        return jsonify(weather_data)  # Return the weather data as JSON
    else:
        return jsonify({"error": "Location not found"}), 404


# Save weather data to the database
def save_weather_data(location, weather_data):
    history_entry = WeatherHistory(
        location=location,
        temperature=weather_data["main"]["temp"],
        description=weather_data["weather"][0]["description"],
    )
    db.session.add(history_entry)
    db.session.commit()


@app.route("/save_favorite", methods=["POST"])
def save_favorite():
    data = request.json
    location = data.get("location")

    if FavoriteLocation.query.filter_by(location=location).first() is None:
        new_favorite = FavoriteLocation(location=location)
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"message": "Location saved as favorite"}), 201
    else:
        return jsonify({"message": "Location is already in favorites"}), 200


@app.route("/favorites", methods=["GET"])
def get_favorites():
    favorites = FavoriteLocation.query.all()
    favorite_locations = [f.location for f in favorites]
    return jsonify(favorite_locations)


@app.route("/weather_history", methods=["GET"])
def get_weather_history():
    history = WeatherHistory.query.order_by(WeatherHistory.timestamp.desc()).all()
    history_data = [
        {
            "location": entry.location,
            "temperature": entry.temperature,
            "description": entry.description,
            "timestamp": entry.timestamp,
        }
        for entry in history
    ]
    return jsonify(history_data)


if __name__ == "__main__":
    app.run(debug=True)
