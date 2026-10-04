from flask import Flask, render_template, request, redirect, flash, url_for
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"   # REQUIRED for flash

# Base price per km for each provider
provider_base_price = {
    "RAPIDO": 10,
    "OLA": 13,
    "UBER": 15
}

# Vehicle multiplier
vehicle_multiplier = {
    "Bike": 1,
    "Car": 2,
    "AC-Car": 2.5,
    "Big Car": 3
}

@app.route("/")
def home():
    return render_template("compare.html")


@app.route("/compare", methods=["POST"])
def compare():

    pickup = request.form["pickup"]
    drop = request.form["drop"]
    vehicle = request.form["vehicle"]

    distance = random.randint(10, 20)

    results = {}

    for provider in provider_base_price:
        base = provider_base_price[provider]
        multiplier = vehicle_multiplier.get(vehicle, 1)  # safe access

        fare = distance * base * multiplier
        fare = round(fare, 2)

        results[provider] = fare

    lowest_provider = min(results, key=results.get)

    return render_template("compare.html",
                           pickup=pickup,
                           drop=drop,
                           vehicle=vehicle,
                           distance=distance,
                           results=results,
                           lowest=lowest_provider)


# ✅ NEW ROUTE FOR BOOKING CONFIRMATION
@app.route("/book", methods=["POST"])
def book():
    flash("🎉 Booking has been confirmed successfully!")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)