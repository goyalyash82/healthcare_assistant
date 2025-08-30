# app.py
from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# --- load diseases.json safely ---
DATA_PATH = os.path.join(os.path.dirname(__file__), "diseases.json")
try:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        diseases = json.load(f)
except FileNotFoundError:
    print(f"ERROR: {DATA_PATH} not found. Create diseases.json in the project folder.")
    diseases = {}
except json.JSONDecodeError as e:
    print(f"ERROR: invalid JSON in {DATA_PATH}: {e}")
    diseases = {}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    # accept either JSON payload or form-data
    if request.is_json:
        payload = request.get_json()
        q = payload.get("disease") or payload.get("symptom") or ""
    else:
        q = request.form.get("disease") or request.form.get("symptom") or ""

    query = q.strip().lower()
    if not query:
        return jsonify({"error": "empty query", "info": None}), 400

    # try exact match, fallback to replace spaces with underscore
    info = diseases.get(query) or diseases.get(query.replace(" ", "_"))
    if not info:
        info = "No information available. Please consult a doctor."

    return jsonify({"disease": query, "info": info})

if __name__ == "__main__":
    print(f"Loaded {len(diseases)} conditions.")
    app.run(debug=True, host="127.0.0.1", port=5000)
