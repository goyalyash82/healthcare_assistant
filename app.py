from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load diseases from JSON file
with open("diseases.json", "r") as f:
    health_tips = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    tip = None
    if request.method == "POST":
        symptom = request.form.get("symptom").lower()
        tip = health_tips.get(
            symptom,
            "⚠️ Sorry, I don’t have advice for that symptom. Please consult a doctor."
        )
    return render_template("index.html", tip=tip)

if __name__ == "__main__":
    app.run(debug=True)

