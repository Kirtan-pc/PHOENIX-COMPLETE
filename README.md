# Phoenix Assistant 🔥

Phoenix is a voice-activated virtual assistant built in Python. It uses speech recognition, text-to-speech, and generative AI to perform tasks like opening websites, playing music, fetching news, and answering questions.

---

## Features

- Voice-activated control
- Opens popular websites (Google, YouTube, Facebook)
- Plays music from a custom library
- Fetches top news headlines via NewsAPI
- Answers questions using Gemini AI (Google's generative model)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/phoenix-assistant.git
cd phoenix-assistant
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

---

## API Keys

You need:

- NewsAPI.org key – for news headlines
- Gemini AI (Google) key – for generative answers

You can hardcode them in `main.py` (as in the example) or store them in a `.env` file (recommended).

---

## Usage

Run the assistant with:

```bash
python main.py
```

Say **"Phoenix"** to activate it, then speak a command like:

- “Open Google”
- “Play [song name]”
- “Give me the news”
- “What is the capital of France?”

Say **"stop"**, **"sleep"**, or **"bye"** to shut it down.

---

## Project Structure

```
phoenix-assistant/
│
├── main.py             # Main assistant script
├── musicLibrary.py     # Dictionary of songs and links
├── requirements.txt    # Python package list
├── .gitignore          # Files/folders Git should ignore
├── README.md           # This file
└── venv/                # Virtual environment (ignored by Git)
```

---

## .gitignore

```
venv/
__pycache__/
*.pyc
.env
```

---

## Notes

- Ensure your microphone works and system permissions allow recording.
- For better API key management, consider using a `.env` file with `python-dotenv`.

---

## License

MIT License

---

## Web Version (Django)

This repo now includes a beginner-friendly web chatbot inside `phoenix_web/`.

### Run the web app

1. Install Django if you have not already:

```bash
pip install -r requirements.txt
```

2. Start the development server:

```bash
cd phoenix_web
python manage.py runserver
```

3. Open the app in your browser:

```
http://127.0.0.1:8000/
```

### How it is organized

- `phoenix_web/chatbot/services/assistant.py` contains the core command logic.
- `phoenix_web/chatbot/services/voice.py` contains placeholders for speech-to-text and text-to-speech.
- `phoenix_web/chatbot/templates/chatbot/index.html` + `static/chatbot/` contain the UI.

### Notes

- The web version avoids paid APIs by default. You can add your own LLM later.
- The original voice assistant remains in `main.py`.
