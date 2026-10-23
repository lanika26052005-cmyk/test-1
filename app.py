from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    foods = [
        {"id": 1, "name": "Burger", "price": 120},
        {"id": 2, "name": "Pizza", "price": 250},
        {"id": 3, "name": "Sandwich", "price": 100},
        {"id": 4, "name": "French Fries", "price": 80}
    ]
    return render_template("index.html", foods=foods)

@app.route("/healthy")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
