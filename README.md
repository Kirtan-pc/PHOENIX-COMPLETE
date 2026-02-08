# PHOENIX Assistant 🔥

**PHOENIX** is a powerful, voice-activated virtual assistant and web-based chatbot built with Python and Django. It leverages cutting-edge AI (Groq/Llama 3), Speech Recognition, and real-time APIs to provide a seamless interactive experience.

---

## 🚀 Features

### 🎧 Voice Assistant (CLI)
- **Voice Activation**: Say "Phoenix" to trigger the assistant.
- **Smart Search**: Integrated with Google and YouTube for instant query results.
- **Entertainment**: Seamless YouTube music playback via voice commands.
- **Web Navigation**: Hands-free control to open popular sites like Facebook, Google, and YouTube.
- **Real-time News**: Fetches top global headlines instantly.

### 💻 Web Chatbot (Django)
- **Modern UI**: Sleek, responsive chat interface.
- **AI Integration**: Powered by Groq (Llama 3) for friendly and intelligent responses.
- **Voice Support**: Built-in speech synthesis (speaking) and recognition.
- **Action-Oriented**: Can execute web actions (like opening URLs) directly from the chat.

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Kirtan-pc/PHOENIX-COMPLETE.git
cd PHOENIX-COMPLETE
```

### 2. Environment Setup
Create a virtual environment and install dependencies:
```bash
# Create venv
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. API Keys Configuration
Create a `.env` file in the root directory and add your keys:
```env
GROQ_API_KEY=your_groq_api_key
NEWS_API_KEY=your_news_api_key
DJANGO_SECRET_KEY=your_django_secret_key
```

---

## 🚀 Running the Apps

### CLI Voice Assistant
```bash
python main.py
```

### Web Dashboard (Django)
```bash
cd phoenix_web
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 📂 Project Structure
```text
PHOENIX/
├── phoenix_web/          # Django Web Application
│   ├── chatbot/          # Chatbot logic, templates, and services
│   └── phoenix_web/      # Project settings
├── main.py               # CLI Voice Assistant Entry Point
├── .env                  # Environment Variables (Ignored by Git)
├── .gitignore            # Git exclusion rules
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 🛡️ Security
This project uses `python-dotenv` to keep sensitive API keys protected. **Never** commit your `.env` file to version control.

## 📄 License
This project is licensed under the MIT License.
