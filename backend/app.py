from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

# In-memory storage for simplicity (replace with a database if needed)
user_profile = {}

@app.route("/api/save-profile", methods=["POST"])
def save_profile():
    global user_profile
    data = request.json
    user_profile = data
    return jsonify({"message": "Profile saved successfully!"})

@app.route("/api/get-profile", methods=["GET"])
def get_profile():
    if user_profile:
        return jsonify(user_profile)
    else:
        return jsonify({})  # No profile yet

@app.route("/api/full-analysis", methods=["POST"])
def full_analysis():
    data = request.json
    profile = data.get("profile", {})
    cycle_phase = data.get("cyclePhase", "menstruation")
    medicine_ingredients = data.get("medicineIngredients", [])
    cosmetic_ingredients = data.get("cosmeticIngredients", [])

    summary = ""

    # -------- Medicine Analysis --------
    conditions = profile.get("conditions", "").lower()
    for med in medicine_ingredients:
        med_lower = med.lower()
        if med_lower == "ibuprofen" and "anemia" in conditions:
            summary += f"- ⚠ {med}: May cause stomach irritation due to anemia.\n"
        if med_lower == "hormone" and "pcos" in conditions:
            summary += f"- ⚠ {med}: Hormonal medicines should be taken carefully with PCOS.\n"
    if not summary:
        summary += "- ✅ No major medicine risks detected.\n"

    # -------- Cosmetic Analysis --------
    for prod in cosmetic_ingredients:
        prod_lower = prod.lower()
        if "alcohol" in prod_lower:
            summary += f"- ⚠ {prod}: May irritate skin, especially during menstruation.\n"
        if "fragrance" in prod_lower:
            summary += f"- ⚠ {prod}: Can cause allergic reactions.\n"
    if not cosmetic_ingredients:
        summary += "- ✅ No cosmetic warnings detected.\n"

    # -------- Cycle-Based Advice --------
    if cycle_phase == "menstruation":
        summary += "- Cycle Advice: Light yoga and stretching recommended.\n"
    elif cycle_phase == "follicular":
        summary += "- Cycle Advice: Strength training and cardio recommended.\n"
    elif cycle_phase == "luteal":
        summary += "- Cycle Advice: Light cardio and walking recommended.\n"
    else:
        summary += "- Cycle Advice: Maintain healthy exercise routine.\n"

    # Optional: Add height/weight advice
    height = profile.get("height")
    weight = profile.get("weight")
    if height and weight:
        bmi = float(weight) / ((float(height)/100)**2)
        summary += f"- BMI: {bmi:.1f}\n"
        if bmi < 18.5:
            summary += "- Advice: Underweight — consider nutrient-rich diet.\n"
        elif bmi > 25:
            summary += "- Advice: Overweight — maintain regular exercise and balanced diet.\n"

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True, port=5000)