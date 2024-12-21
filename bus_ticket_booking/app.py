from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "69106372e709602b4b70138c6917c22f"

# Define bus routes, prices, and initial seat availability
bus_routes = {
    "Route 1 (Pattukkottai to Coimbatore)": {
        "landmarks": ["Pattukkottai", "Palladam", "karanampettai","Sulur","Pappampatti Pirivu","Ondipudur","Singanallur","Hopes College" "Gandhipuram"],
        "regular": [True, True, False, True, True],
        "sleeper": [True, False, True, True]
    },
    "Route 2 (Coimbatore to Vedaranyam)": {
        "landmarks": ["Gandhipuram","Hopes College","Singanallur" ,"Ondipudur","Pappampatti Pirivu", "Sulur" ,"karanampettai","Palladam","Patukottai","Muthupettai","Vedaranyam"],
        "regular": [True, True, True, True, False],
        "sleeper": [False, True, True, True]
    }
}

seat_prices = {"regular": 500, "sleeper": 800}

@app.route("/")
def home():
    return render_template("home.html", routes=bus_routes)

@app.route("/book/<route_name>", methods=["GET", "POST"])
def book(route_name):
    route = bus_routes.get(route_name)
    if not route:
        return "Route not found", 404
    
    if request.method == "POST":
        seat_type = request.form.get("seat_type")
        seat_number = int(request.form.get("seat_number"))
        
        # Validate seat type and availability
        if seat_type in route and 0 < seat_number <= len(route[seat_type]):
            if route[seat_type][seat_number - 1]:
                route[seat_type][seat_number - 1] = False
                total_price = seat_prices[seat_type]
                return render_template("success.html", route=route_name, seat_type=seat_type, seat_number=seat_number, total_price=total_price)
            else:
                return render_template("error.html", message="Seat already booked.")
        else:
            return render_template("error.html", message="Invalid seat type or number.")
    return render_template("book.html", route_name=route_name, route_data=route)

@app.route("/cancel/<route_name>", methods=["GET", "POST"])
def cancel(route_name):
    route = bus_routes.get(route_name)
    if not route:
        return "Route not found", 404
    
    if request.method == "POST":
        seat_type = request.form.get("seat_type")
        seat_number = int(request.form.get("seat_number"))
        
        # Validate seat type and availability
        if seat_type in route and 0 < seat_number <= len(route[seat_type]):
            if not route[seat_type][seat_number - 1]:
                route[seat_type][seat_number - 1] = True
                return render_template("success.html", route=route_name, action="cancel")
            else:
                return render_template("error.html", message="Seat not booked.")
        else:
            return render_template("error.html", message="Invalid seat type or number.")
    return render_template("cancel.html", route_name=route_name)

if __name__ == "__main__":
    app.run(debug=True)
