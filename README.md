# 🧠✨ NeuroNest AI  
*Empathetic. Intelligent. Secure.*

---

## 💬 Overview  
**NeuroNest AI** is a smart, web-based chatbot designed for empathetic and human-like conversations. Powered by Google's **Gemini API**, it offers a secure multi-user environment with dynamic personality switching and a sleek modern interface.

---

## 🔑 Key Features  

- 🔐 **Secure User Authentication**  
  Robust registration & login system with password encryption using **Bcrypt**, ensuring data privacy and persistence.

- 🤖 **AI-Powered Conversations**  
  Integrated with **Google Gemini API** to deliver human-like, context-aware responses.

- 🔄 **Switchable Personalities**  
  Choose from multiple chatbot personas:  
  - 🧘‍♀️ Calm Therapist  
  - 👯 Friendly Buddy  
  - 👂 Supportive Listener

- 🛡️ **Admin Dashboard**  
  `/admin` route allows users with the **admin role** to view all registered users and access full chat logs.

- 🌐 **Modern Frontend**  
  Clean and responsive UI using **HTML5, CSS3 (Flexbox)**, and **JavaScript (Fetch API)**, featuring:  
  - Animated splash screen  
  - Typewriter effect for bot messages

---

## 🛠️ Tech Stack  

| Category       | Technology                          |
|----------------|-------------------------------------|
| **Backend**    | Flask, Flask-Bcrypt                 |
| **Database**   | MongoDB                             |
| **AI**         | Google Generative AI (Gemini)       |
| **Frontend**   | HTML5, CSS3 (Flexbox), JavaScript   |

---

## 🚀 Getting Started  

### ✅ Prerequisites  
- Python 3.8+  
- MongoDB (running locally)  
- A valid **Google Gemini API Key**

---

## 🧪 Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/neuronest-ai.git
cd neuronest-ai
```

### 2. Create and Activate Virtual Environment  
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies  
```bash
pip install Flask Flask-Bcrypt pymongo google-generativeai python-dotenv
```

### 4. Set Environment Variables  
Create a `.env` file in the root directory with the following:
```
GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

Update your Python files (`app.py` and `chatbot.py`) with:
```python
from dotenv import load_dotenv
load_dotenv()
```

And in `chatbot.py`:
```python
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
```

---

## ▶️ Run the Application  
```bash
python app.py
```
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 👑 Admin Access Setup  

1. Register a new user via the app.  
2. Open **MongoDB Compass** or the shell.  
3. Navigate to the `neuronest` database → `users` collection.  
4. Find the user and change their role to:  
   ```json
   "role": "admin"
   ```  
5. Log in with the updated credentials to access admin features.

---