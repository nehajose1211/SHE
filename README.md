<p align="center">
  <img src="https://images.unsplash.com/photo-1596462502278-27bfdc403348" alt="HerBalance Banner" width="100%">
</p>

# 🌸 HerBalance 🎯

## Basic Details

### Team Name: [SHE]

### Team Members
- **Neha Jose** - [College Of Engineering Chengannur]
- **Ananya P Santh** - [College Of Engineering Chengannur]

### Hosted Project Link
[[Link to hosted Flask application](https://she-apdl.onrender.com/)]

### Project Description
[cite_start]HerBalance is an AI-powered health assistant designed to provide women with a safe space to manage their health. [cite_start]It integrates menstrual cycle tracking with intelligent ingredient analysis for medicines and cosmetics to provide personalized safety advice.

### The Problem Statement
[cite_start]Women often lack immediate, personalized insights into how their menstrual cycle phases or existing health conditions (like PCOS or anemia) interact with daily medications and cosmetic products[cite: 7, 52].

### The Solution
[cite_start]We developed a platform that combines **OCR (Optical Character Recognition)** for scanning labels with **LLM-based AI** to analyze risks[cite: 37, 84]. [cite_start]The system alerts users to hormonal disruptors and harmful drug interactions specific to their profile[cite: 10].

---

## Technical Details

### Technologies/Components Used

**For Software:**
- [cite_start]**Languages:** Python (Backend), JavaScript (Frontend), HTML5, CSS3[cite: 1, 47, 89].
- [cite_start]**Frameworks:** Flask.
- [cite_start]**Libraries:** - `Tesseract.js`: For client-side image-to-text processing[cite: 37].
  - [cite_start]`OpenAI SDK`: To interface with OpenRouter AI models.
  - [cite_start]`Flask-CORS`: For handling cross-origin requests.
  - [cite_start]`python-dotenv`: For secure API key management.
- [cite_start]**Tools:** VS Code, OpenRouter (NVIDIA Nemotron-3 model).

---

## Features

- [cite_start]**📅 Cycle Dashboard:** Predicts the next period based on user-defined cycle length and provides phase-specific workout and food suggestions[cite: 44, 60, 69].
- [cite_start]**💄 Cosmetic Analyzer:** Uses Tesseract.js to extract text from product images and identifies irritants like parabens, sulfates, and triclosan[cite: 37, 39].
- [cite_start]**💊 Medicine Safety Checker:** Compares medications against conditions like PCOS, anemia, and diabetes to flag specific risks (e.g., Ibuprofen risks for anemia).
- [cite_start]**🤖 AI Risk Analysis:** A "Full Analysis" feature that correlates profile data, cycle phase, and scanned ingredients using AI to identify hormonal disruptors[cite: 6, 10, 85].
- [cite_start]**👤 Health Profile:** Stores user metrics (age, height, weight) and health history locally to customize analysis[cite: 55, 72].

---

## Implementation

### Installation
```bash
# Clone the repository
git clone [https://github.com/nehajose1211/SHE]

# Install required dependencies
cd backend
pip install -r requirements.txt