from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("API_KEY"),
)

def chat_ai(message):
    response = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-30b-a3b:free",
        messages=[
            {
                "role": "system", 
                "content": "You are HerBalance AI, a helpful health assistant for women. Provide brief, clear, and safe advice about medicines and cosmetic ingredients based on the user's profile."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return response.choices[0].message.content

# 1. SETUP PATHS (The "Jumper" Logic)
# This gets the absolute path of the 'backend' folder
backend_dir = os.path.dirname(os.path.abspath(__file__))
# This moves up one level to the root, then into 'frontend'
frontend_dir = os.path.abspath(os.path.join(backend_dir, '..', 'frontend'))

# 2. LOAD ENVIRONMENT
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
HF_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

# 3. INITIALIZE FLASK
# template_folder tells Flask where index.html is
# static_folder/static_url_path tells Flask where CSS/JS files are
app = Flask(__name__, 
            template_folder=frontend_dir, 
            static_folder=frontend_dir, 
            static_url_path='')
CORS(app)

# In-memory storage for simplicity
user_profile = {}

# =======================
# ROUTES
# =======================

@app.route("/")
def index():
    """Directly shows the index page from the frontend folder"""
    return render_template("index.html")

@app.route("/api/save-profile", methods=["POST"])
def save_profile():
    global user_profile
    data = request.json
    user_profile = data
    return jsonify({"message": "Profile saved successfully!"})

@app.route("/api/get-profile", methods=["GET"])
def get_profile():
    return jsonify(user_profile if user_profile else {})

@app.route("/api/full-analysis", methods=["POST"])
def full_analysis():
    data = request.json
    profile = data.get("profile", {})
    cycle_phase = data.get("cyclePhase", "Not specified")
    medicine_ingredients = data.get("medicineIngredients", [])
    cosmetic_ingredients = data.get("cosmeticIngredients", [])

    prompt = (
        f"Analyze risks for a user with this profile: {profile}. "
        f"Current cycle phase: {cycle_phase}. "
        f"Medicines to check: {medicine_ingredients}. "
        f"Cosmetic ingredients: {cosmetic_ingredients}. "
        f"Please identify any harmful interactions or hormonal disruptors."
    )

    try:
        ai_summary = chat_ai(prompt)
    except Exception as e:
        ai_summary = f"Error in AI processing: {str(e)}"

    return jsonify({"summary": ai_summary})

# =======================
# RUN SERVER
# =======================
port = os.getenv("PORT")
if __name__ == "__main__":
    # Check if the path actually exists before starting
    if not os.path.exists(os.path.join(frontend_dir, "index.html")):
        print(f"ERROR: Could not find index.html in {frontend_dir}")
    else:
        print(f"Success! Serving frontend from: {frontend_dir}")
        app.run(debug=True, port=port)

