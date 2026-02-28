// ==========================================
// 1. PERIOD TRACKER & DASHBOARD LOGIC
// ==========================================
function predictPeriod() {
    const lastDateInput = document.getElementById("lastPeriod")?.value;
    const cycleLengthInput = parseInt(document.getElementById("cycleLength")?.value);
    const resultElement = document.getElementById("result");

    if (!lastDateInput || isNaN(cycleLengthInput)) {
        alert("Please enter Last Period Date and Cycle Length.");
        return;
    }

    // T00:00:00 ensures date is treated as local time, not UTC
    const lastDate = new Date(lastDateInput + 'T00:00:00');
    const nextPeriodDate = new Date(lastDate);
    nextPeriodDate.setDate(lastDate.getDate() + cycleLengthInput);

    if (resultElement) {
        resultElement.innerHTML = `<strong>Next Period:</strong> ${nextPeriodDate.toDateString()}`;
    }

    // Calculate current cycle day for suggestions
    const today = new Date();
    today.setHours(0, 0, 0, 0); 
    const diffTime = today - lastDate;
    const daysSinceLastPeriod = Math.floor(diffTime / (1000 * 60 * 60 * 24)) + 1;
    const cycleDay = ((daysSinceLastPeriod - 1) % cycleLengthInput) + 1;

    detectPhase(cycleDay);
}

function detectPhase(cycleDay) {
    const wDiv = document.getElementById("workout");
    const fDiv = document.getElementById("food");
    if (!wDiv || !fDiv) return;

    let workout = "";
    let food = "";

    if (cycleDay >= 1 && cycleDay <= 5) {
        workout = '<h3>Recommended</h3><ul><li>Light yoga</li><li>Walking</li></ul>';
        food = '<h3>Recommended</h3><ul><li>Iron-rich foods</li><li>Warm soups</li></ul>';
    } else if (cycleDay >= 6 && cycleDay <= 13) {
        workout = '<h3>Recommended</h3><ul><li>Strength training</li><li>Cardio</li></ul>';
        food = '<h3>Recommended</h3><ul><li>Lean protein</li><li>Nuts</li></ul>';
    } else {
        workout = '<h3>Recommended</h3><ul><li>Pilates</li><li>Stretching</li></ul>';
        food = '<h3>Recommended</h3><ul><li>Healthy fats</li><li>Magnesium</li></ul>';
    }

    wDiv.innerHTML = workout;
    fDiv.innerHTML = food;
}

// ==========================================
// 2. PROFILE SAVE/EDIT/VIEW (With Safety Checks)
// ==========================================
function initProfile() {
    const profileForm = document.getElementById("profileForm");
    const editBtn = document.getElementById("editBtn");
    const cancelBtn = document.getElementById("cancelBtn");

    if (profileForm) {
        profileForm.addEventListener("submit", function(e) {
            e.preventDefault();
            const profile = {
                Name: document.getElementById("Name").value,
                age: document.getElementById("age").value,
                height: document.getElementById("height").value,
                weight: document.getElementById("weight").value,
                conditions: document.getElementById("conditions").value,
                medicines: document.getElementById("medicines").value,
                Allergies: document.getElementById("Allergies").value
            };
            localStorage.setItem("profile", JSON.stringify(profile));
            alert("Profile Saved!");
            updateProfileUI();
        });
    }

    if (editBtn) {
        editBtn.addEventListener("click", () => {
            document.getElementById("profileForm").style.display = "block";
            document.getElementById("profileView").style.display = "none";
        });
    }

    if (cancelBtn) {
        cancelBtn.addEventListener("click", updateProfileUI);
    }

    updateProfileUI();
}

function updateProfileUI() {
    const savedProfile = localStorage.getItem("profile");
    const showProfile = document.getElementById("showProfile");
    const profileView = document.getElementById("profileView");
    const profileForm = document.getElementById("profileForm");

    if (!showProfile || !savedProfile) return;

    const profile = JSON.parse(savedProfile);
    showProfile.innerHTML = `
        <strong>Name:</strong> ${profile.Name} <br>
        <strong>Age:</strong> ${profile.age} <br>
        <strong>Conditions:</strong> ${profile.conditions}
    `;

    if (profileView) profileView.style.display = "block";
    if (profileForm) profileForm.style.display = "none";
}

// ==========================================
// 3. AI ANALYSIS
// ==========================================
async function runAIAnalysis() {
    const aiResultDiv = document.getElementById("aiResult");
    const savedProfile = localStorage.getItem("profile");
    
    // 1. Check if profile exists
    if (!savedProfile) {
        alert("Please complete your Personal Profile first!");
        return;
    }

    // 2. Gather data from the page
    const profile = JSON.parse(savedProfile);
    const medicineInput = document.getElementById("medicine")?.value || "";
    const cosmeticInput = document.getElementById("ingredients")?.innerText || ""; // From Tesseract
    
    aiResultDiv.innerHTML = "⏳ AI is thinking... please wait.";

    try {
        const response = await fetch("http://localhost:5000/api/full-analysis", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                profile: profile,
                cyclePhase: "Not specified", // You can expand this later
                medicineIngredients: medicineInput.split(","),
                cosmeticIngredients: cosmeticInput.split(",")
            })
        });

        const data = await response.json();
        
        // 3. Display the result
        aiResultDiv.innerHTML = `
            <div style="background: #fdf2f8; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4da6; margin-top: 10px;">
                <strong>🤖 AI Analysis:</strong><br>${data.summary}
            </div>`;
    } catch (error) {
        aiResultDiv.innerHTML = "❌ Error connecting to AI server. Make sure app.py is running.";
        console.error(error);
    }
}

// Start Profile logic when page loads
document.addEventListener("DOMContentLoaded", initProfile);
