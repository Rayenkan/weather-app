from flask import Flask, render_template ,request
from geopy.geocoders import Nominatim
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weatherimg=""
    temp=""
    desc=""
    place=""
    if request.method == 'POST':
        try :
            place=request.form["place"]
            geolocator = Nominatim(user_agent="my_geocoding_app")
            location = geolocator.geocode(place)
            lat=location.latitude
            lon=location.longitude
            result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=4a878ed39f73fffe6591a2aa5da230d2")
            details=result.json()
            weatherimg="https://openweathermap.org/img/wn/" +details["weather"][0]["icon"]+"@2x.png"
            temp=str(round(details["main"]["temp"]-273.15))+"°C"
            desc=str(details["weather"][0]["main"])
        except :
            weatherimg=""
            temp=""
            desc=""
            place="Place not Found"

    return render_template("index.html" , place=place , weatherimg=weatherimg , temp=temp , desc=desc)
if __name__ == '__main__':
    app.run(debug=False , host='0.0.0.0')

