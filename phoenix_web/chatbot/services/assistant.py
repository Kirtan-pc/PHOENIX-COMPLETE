import os
import requests
import re
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env')

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

OFFLINE_RESPONSES = {
    "hello": "Hello! I'm operating in low-power mode (Rate Limit), but I'm here.",
    "hi": "Hi there! I'm cooling down my AI processors, but I can still run commands.",
    "hey": "Hey! I'm taking a short break from the cloud, but I'm listening.",
    "phoenix": "I'm here! (Offline Mode active)",
    "how are you": "I'm doing well, just waiting for my rate limit to reset.",
}

def get_offline_fallback(text):
    text = text.lower().strip()
    for key, response in OFFLINE_RESPONSES.items():
        if key in text:
            return response
    return None

def ask_groq(prompt_text):
    """Query Groq API."""
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "system", 
                    "content": "You are PHOENIX, a helpful voice assistant. Give SHORT, SIMPLE, and FRIENDLY responses (2-3 sentences max). Be conversational and natural, like talking to a friend. Avoid long explanations unless specifically asked."
                },
                {"role": "user", "content": prompt_text}
            ]
        }
        
        print(f"[Groq] Querying AI...")
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        elif response.status_code == 429:
            # Rate limit - try offline fallback
            fallback = get_offline_fallback(prompt_text)
            if fallback:
                return fallback
            return "I'm experiencing high demand. Please try again in a moment."
        else:
            print(f"[Groq Error]: {response.status_code} - {response.text}")
            fallback = get_offline_fallback(prompt_text)
            if fallback:
                return fallback
            return f"Sorry, I couldn't connect. Error code: {response.status_code}"
            
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except Exception as e:
        print(f"[Groq Exception]: {str(e)}")
        fallback = get_offline_fallback(prompt_text)
        if fallback:
            return fallback
        return f"Sorry, I encountered an error: {str(e)}"

def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            headlines = [article["title"] for article in articles[:5]]
            return "Here are the top 5 headlines: " + ". ".join(headlines)
        return "I couldn't fetch the news right now."
    except Exception:
        return "Error fetching news."

def process_command(command):
    text = command.strip().lower()



    # Browser shortcuts
    if 'open google' in text:
        return {'reply': 'Opening Google.', 'action': {'type': 'open_url', 'url': 'https://www.google.com'}}
    if 'open youtube' in text:
        return {'reply': 'Opening YouTube.', 'action': {'type': 'open_url', 'url': 'https://www.youtube.com'}}
    if 'open facebook' in text:
        return {'reply': 'Opening Facebook.', 'action': {'type': 'open_url', 'url': 'https://www.facebook.com'}}

    # Explicit Search Commands
    # Google Search
    if 'google' in text and ('search' in text or 'find' in text):
        # Pattern: "search/find [query] on/in google"
        match = re.search(r'(?:search|find) (.+) (?:on|in) google', text)
        if match:
            query = match.group(1).strip()
            return {
                'reply': f"Searching Google for {query}...",
                'action': {'type': 'open_url', 'url': f"https://www.google.com/search?q={query}"}
            }
        
        # Pattern: "search/find google for [query]"
        match = re.search(r'(?:search|find) google for (.+)', text)
        if match:
            query = match.group(1).strip()
            return {
                'reply': f"Searching Google for {query}...",
                'action': {'type': 'open_url', 'url': f"https://www.google.com/search?q={query}"}
            }

    # YouTube Search
    if 'youtube' in text and ('search' in text or 'find' in text):
        # Pattern: "search/find [query] on/in youtube"
        match = re.search(r'(?:search|find) (.+) (?:on|in) youtube', text)
        if match:
            query = match.group(1).strip()
            return {
                'reply': f"Searching YouTube for {query}...",
                'action': {'type': 'open_url', 'url': f"https://www.youtube.com/results?search_query={query}"}
            }

        # Pattern: "search/find youtube for [query]"
        match = re.search(r'(?:search|find) youtube for (.+)', text)
        if match:
            query = match.group(1).strip()
            return {
                'reply': f"Searching YouTube for {query}...",
                'action': {'type': 'open_url', 'url': f"https://www.youtube.com/results?search_query={query}"}
            }

    # Play music (Direct YouTube Search)
    if text.startswith('play '):
        song = text.replace('play', '', 1).strip()
        return {
            'reply': f"Playing {song} on YouTube.",
            'action': {'type': 'open_url', 'url': f"https://www.youtube.com/results?search_query={song}"}
        }

    # News
    if 'news' in text:
        return {'reply': get_news()}

    # Closing
    if any(phrase in text for phrase in ['stop', 'sleep', 'bye']):
        return {'reply': 'Goodbye! I will be here if you need me.'}

    # Default fallback to AI
    ai_reply = ask_groq(command)
    return {'reply': ai_reply}

