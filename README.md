<h1 align="center" id="title">StarMedic</h1>
<p align="center">
  <img src="https://github.com/ShrawanSai/StarMedic/blob/main/screenshots/logo.jpg" alt="project-screenshot" width="200" height="200">
</p>


<p align="center"><img src="https://socialify.git.ci/ShrawanSai/StarMedic/image?description=1&amp;descriptionEditable=The%20Star%20Wars%20Medical%20Diagnosis%20Game!&amp;font=Raleway&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Diagonal%20Stripes&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>


<p id="description">Embark on a thrilling journey through the Star Wars universe as a skilled medic. Your mission is to diagnose and treat patients from various species across the galaxy. Engage in interactive dialogues ask probing questions and choose the right options to uncover mysterious ailments. Earn points for accurate diagnoses and effective treatment plans. The more precise you are the higher your score will soar. Are you ready to use your medical skills to save lives in a galaxy far far away? Dive in and may the Force be with you!</p>

<h2>🚀 Demo</h2>

1. [Streamlit Live link](https://starmedic.streamlit.app/)
2. [Youtube Video](https://www.youtube.com/watch?v=R_4jrGhQ7Yo&t=3s)


<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Interactive Dialogue System: Players interact with various characters who guide them through the diagnosis and treatment process.
*   Dynamic Scenarios: Each game session features randomly generated patients and diseases ensuring a unique experience every time.
*   Educational Gameplay: Players learn about different diseases symptoms and treatment options through a gamified experience.
*   Multi-LLM Integration: The game uses different LLMs to manage situations generate dialogues reason through diseases and create decision-making options.

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository:</p>

```
git clone https://github.com/ShrawanSai/StarMedic.git
```

<p>2. Enter into Directory</p>

```
cd StarMedic
```

<p>3. Create new virtual environment (Optional)</p>

<p>4. Install Requirements</p>

```
pip install -r requirements.txt
```

<p>5. Create a .env file and add your Gemini API Key in the file</p>

```
GOOGLE_API_KEY = YOUR-API-KEY
```

<p>6. Run Streamlit application using</p>

```
streamlit run situation.py
```


## 🧩 How It Works

StarMedic is built around an interactive gameplay loop where players diagnose and treat patients from various species in the Star Wars universe. The game is structured as follows:

1. **Random Patient Selection**: A patient with a randomly generated disease and symptoms is selected from the database.
  
2. **Dialogue and Decision-Making**: 
   - The Situation LLM creates the context and sets the scene by reviewing patient information.
   - The Actor LLM takes the role of a character within the game, engaging the player in dialogue.
   - Players can ask questions, suggest tests, or directly make a diagnosis by selecting from multiple options.
  
3. **Processing and Feedback**:
   - The Disease Reasoning LLM interprets the player's inputs, checks if they correspond to symptoms, and offers clarifications or test results.
   - If the player selects a correct diagnosis, the game proceeds to provide positive feedback; if incorrect, hints are given to guide them toward the right diagnosis.
   - The Options LLM dynamically generates and presents new choices based on the context of the game.

4. **Game Continuation**:
   - Players continue making decisions and engaging in dialogues until they correctly diagnose the patient's condition or the game ends.
  
5. **Scoring**:
   - Points are awarded based on the accuracy and efficiency of the player's decisions, encouraging them to hone their diagnostic skills.

[View the UML Diagram](https://github.com/ShrawanSai/StarMedic/blob/main/MedicalGame.drawio.png) for a detailed visual representation of the game's flow.

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Google Gemini API
*   Python
*   Streamlit
