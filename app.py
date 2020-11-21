from flask import Flask, render_template, request, redirect, url_for
import io
from flask import Response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/handleCafeRacer", methods=['GET'])
def handleCafeRacer():
    return redirect("https://www.bikeexif.com/tag/cafe-racer")

@app.route("/handleRaceBike", methods=['GET'])
def handleRaceBike():
    return redirect("https://www.drivespark.com/bikes/sports/")

@app.route("/handlePremiumStreetBike", methods=['GET'])
def handlePremiumStreetBike():
    return redirect("https://gaadiwaadi.com/top-10-selling-premium-bikes-rs-2-lakh-segment-in-india-during-fy20/")

@app.route("/handlePremiumAdventure", methods=['GET'])
def handlePremiumAdventure():
    return redirect("https://www.carandbike.com/news/top-7-premium-adventure-touring-motorcycles-in-india-2252798")

@app.route("/handleSportyCafe", methods=['GET'])
def handleSportyCafe():
    return redirect("https://www.topspeed.com/motorcycles/guides/top-10-cafe-racers-of-2018-ar182710.html")

@app.route("/handleAdventureTourer", methods=['GET'])
def handleAdventureTourer():
    return redirect("https://www.bforbiker.com/adventure-bikes-in-india/")

@app.route("/handleCruiser", methods=['GET'])
def handleCruiser():
    return redirect("https://www.zigwheels.com/newbikes/best-cruiser-bikes")

@app.route("/handleSuperBike", methods=['GET'])
def handleSuperBike():
    return redirect("https://www.bikedekho.com/upcoming-bikes/super")



if __name__ == "__main__":
    app.run(debug=True)
