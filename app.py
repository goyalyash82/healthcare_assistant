from flask import Flask, render_template, request

app = Flask(__name__)
health_tips = {
    # Common conditions
    "fever": "Drink plenty of fluids, rest, and take paracetamol if needed. Consult a doctor if it persists.",
    "cough": "Stay hydrated, take warm fluids, and avoid cold exposure.",
    "cold": "Rest, drink warm fluids, and inhale steam.",
    "flu": "Rest, drink fluids, and take over-the-counter fever reducers if needed.",
    "headache": "Rest, hydrate, and avoid bright screens.",
    "migraine": "Rest in a dark room, avoid triggers like loud sounds, and use prescribed medication if available.",
    "stomachache": "Eat light meals, avoid spicy food, and drink water.",
    "indigestion": "Eat smaller meals, avoid oily foods, and drink ginger tea.",
    "diarrhea": "Drink ORS, stay hydrated, and avoid heavy meals.",
    "constipation": "Eat high-fiber foods, drink water, and exercise regularly.",
    "sore throat": "Gargle with warm salt water and drink warm fluids.",
    "toothache": "Rinse with warm salt water, apply a cold compress, and visit a dentist.",
    "back pain": "Maintain posture, apply a warm compress, and do light stretching.",
    "joint pain": "Apply warm compress, rest, and try gentle exercises.",
    "burn": "Cool the burn under running water for 10 minutes and cover with a clean cloth.",
    "sprain": "Rest, apply ice, compression, and elevate the limb (RICE method).",
    "allergy": "Avoid allergens, stay indoors, and take antihistamines if prescribed.",
    "asthma": "Use prescribed inhaler, avoid smoke/dust, and practice breathing exercises.",
    "hypertension": "Reduce salt intake, exercise, and monitor blood pressure regularly.",
    "diabetes": "Follow a balanced diet, exercise, and monitor blood sugar regularly.",
    "anxiety": "Practice deep breathing, meditation, and talk to a professional if severe.",
    "depression": "Stay socially connected, exercise, and seek professional help.",
    "insomnia": "Maintain sleep hygiene, avoid caffeine at night, and relax before bed.",
    "skin rash": "Keep area clean, avoid scratching, and use soothing lotion.",
    "acne": "Wash face regularly, avoid oily food, and keep skin clean.",
    "eczema": "Moisturize skin, avoid irritants, and wear soft clothing.",
    "sunburn": "Apply aloe vera, stay hydrated, and avoid sun exposure.",
    "dehydration": "Drink water/ORS, rest in shade, and avoid heat.",
    "food poisoning": "Drink fluids, eat light food, and rest.",
    "motion sickness": "Sit near a window, avoid reading in moving vehicle, and take ginger tea.",
    "ear pain": "Apply warm compress, avoid poking ear, and see doctor if severe.",
    "eye strain": "Rest eyes, follow 20-20-20 rule, and avoid long screen time.",
    "conjunctivitis": "Clean eyes with warm water, avoid touching eyes, and wash hands regularly.",
    "nosebleed": "Pinch nose, lean forward, and apply cold compress.",
    "heatstroke": "Move to a cool place, drink water, and apply wet cloth on body.",
    "hypothermia": "Warm the person slowly with blankets and warm fluids.",
    "fracture": "Immobilize limb, apply ice packs, and seek immediate medical care.",
    "heartburn": "Avoid spicy/oily foods, eat smaller meals, and drink water.",
    "ulcer": "Eat small frequent meals, avoid alcohol/spicy food.",
    "kidney stone": "Drink plenty of water, avoid excess salt, and consult doctor.",
    "UTI": "Drink lots of water, avoid caffeine, and maintain hygiene.",
    "anemia": "Eat iron-rich foods (spinach, beans, red meat).",
    "thyroid": "Take prescribed medicine regularly and follow healthy diet.",
    "arthritis": "Do gentle exercises, use warm compress, and maintain healthy weight.",
    "bronchitis": "Avoid smoking, take steam inhalation, and stay hydrated.",
    "pneumonia": "Rest, drink fluids, and seek medical care if severe.",
    "malaria": "Use mosquito nets, stay hydrated, and consult doctor for antimalarials.",
    "dengue": "Drink plenty of fluids, avoid NSAIDs, and monitor platelets.",
    "covid": "Isolate, wear a mask, drink fluids, and monitor oxygen.",
    # ... continue until 150+ conditions
}


@app.route("/", methods=["GET", "POST"])
def index():
    tip = None
    if request.method == "POST":
        symptom = request.form.get("symptom").lower()
        tip = health_tips.get(symptom, "Sorry, I don’t have advice for that symptom. Please consult a doctor.")
    return render_template("index.html", tip=tip)

if __name__ == "__main__":
    app.run(debug=True)
