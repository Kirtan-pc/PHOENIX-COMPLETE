const chat = document.getElementById('chat');
const input = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const voiceBtn = document.getElementById('voiceBtn');

// Voice Recognition Setup
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition;
if (SpeechRecognition) {
  recognition = new SpeechRecognition();
  recognition.continuous = false;
  recognition.lang = 'en-US';
  recognition.interimResults = false;

  recognition.onstart = () => {
    voiceBtn.classList.add('active');
  };

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    input.value = transcript;
    sendMessage(true);
  };

  recognition.onend = () => {
    voiceBtn.classList.remove('active');
  };
}

// Voice Synthesis (Speaking)
function speak(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.rate = 1;
  utterance.pitch = 1;
  window.speechSynthesis.speak(utterance);
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return '';
}

function addMessage(text, sender) {
  const bubble = document.createElement('div');
  bubble.className = `bubble ${sender}`;
  bubble.textContent = text;
  chat.appendChild(bubble);
  chat.scrollTop = chat.scrollHeight;

  // Remove welcome message on first activity
  const welcome = document.querySelector('.welcome-message');
  if (welcome) welcome.style.display = 'none';
}

async function sendMessage(isVoice = false) {
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, 'user');
  input.value = '';

  try {
    const response = await fetch('/api/chat/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();
    if (data.reply) {
      addMessage(data.reply, 'bot');
      if (isVoice) {
        speak(data.reply); // Only speak if input was voice
      }
    }

    if (data.action && data.action.type === 'open_url') {
      window.open(data.action.url, '_blank');
    }
  } catch (err) {
    console.error("Chat Error:", err);
    addMessage(`I'm having trouble connecting (Error: ${err.message}). Please check the console.`, 'bot');
  }
}

sendBtn.addEventListener('click', () => sendMessage(false));
input.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    sendMessage(false);
  }
});

voiceBtn.addEventListener('click', () => {
  if (recognition) {
    recognition.start();
  } else {
    alert("Speech recognition is not supported in this browser.");
  }
});

