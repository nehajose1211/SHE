<p align="center">
  <img src="https://raw.githubusercontent.com/tinkerhub/tink-her-hack-temp/main/img.png" alt="HerBalance Banner" width="100%">
</p>

# 🌸 HerBalance 🎯

## Basic Details

### Team Name: SHE

### Team Members
- **Neha Jose** - College Of Engineering Chengannur
- **Ananya P Santh** - College Of Engineering Chengannur

### Hosted Project Link
[[Link to hosted Flask application](https://she-apdl.onrender.com/)]

### Project Description
HerBalance is an AI-powered health assistant designed to provide women with a safe space to manage their health. It integrates menstrual cycle tracking with intelligent ingredient analysis for medicines and cosmetics to provide personalized safety advice.

### The Problem Statement
Women often lack immediate, personalized insights into how their menstrual cycle phases or existing health conditions (like PCOS or anemia) interact with daily medications and cosmetic products.

### The Solution
We developed a platform that combines **OCR (Optical Character Recognition)** for scanning labels with **LLM-based AI** to analyze risks. The system alerts users to hormonal disruptors and harmful drug interactions specific to their profile.

---

## Technical Details

### Technologies/Components Used

**For Software:**
- **Languages:** Python (Backend), JavaScript (Frontend), HTML5, CSS3.
- **Frameworks:** Flask.
- **Libraries:** - `Tesseract.js`: For client-side image-to-text processing.
  - `OpenAI SDK`: To interface with OpenRouter AI models.
  - `Flask-CORS`: For handling cross-origin requests.
  - `python-dotenv`: For secure API key management.
- **Tools:** VS Code, OpenRouter (NVIDIA Nemotron-3 model).

---

## Features

- **📅 Cycle Dashboard:** Predicts the next period based on user-defined cycle length and provides phase-specific workout and food suggestions.
- **💄 Cosmetic Analyzer:** Uses Tesseract.js to extract text from product images and identifies irritants like parabens, sulfates, and triclosan.
- **💊 Medicine Safety Checker:** Compares medications against conditions like PCOS, anemia, and diabetes to flag specific risks (e.g., Ibuprofen risks for anemia).
- **🤖 AI Risk Analysis:** A "Full Analysis" feature that correlates profile data, cycle phase, and scanned ingredients using AI to identify hormonal disruptors.
- **👤 Health Profile:** Stores user metrics (age, height, weight) and health history locally to customize analysis.

---

## Implementation

### Installation
```bash
# Clone the repository
git clone [https://github.com/nehajose1211/SHE]

# Install required dependencies
cd backend
pip install -r requirements.txt