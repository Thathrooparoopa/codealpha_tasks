/* ---------------------------------
   FAQ Suggestions (Auto-suggest)
---------------------------------- */
const faqSuggestions = [
    "What are OPD timings?",
    "Is emergency service available 24/7?",
    "How can I book an appointment?",
    "Do you accept insurance?",
    "Is ICU available?",
    "Is pharmacy open 24 hours?",
    "Is parking available?",
    "Do you have laboratory services?"
];

/* ---------------------------------
   DOM Elements
---------------------------------- */
const inputBox = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const typingIndicator = document.getElementById("typing-indicator");
const suggestionsBox = document.getElementById("suggestions");

/* ---------------------------------
   Send Message Function
---------------------------------- */
function sendMessage() {
    const message = inputBox.value.trim();
    if (!message) return;

    // Show user message
    const userDiv = document.createElement("div");
    userDiv.className = "user-msg";
    userDiv.innerText = message;
    chatBox.appendChild(userDiv);

    inputBox.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    // Hide suggestions after sending
    if (suggestionsBox) {
        suggestionsBox.classList.add("hidden");
    }

    // Show typing indicator
    if (typingIndicator) {
        typingIndicator.classList.remove("hidden");
    }

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        if (typingIndicator) {
            typingIndicator.classList.add("hidden");
        }

        const botDiv = document.createElement("div");
        botDiv.className = "bot-msg";
        botDiv.innerText = "😊 " + data.reply;
        chatBox.appendChild(botDiv);

        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(() => {
        if (typingIndicator) {
            typingIndicator.classList.add("hidden");
        }

        const errorDiv = document.createElement("div");
        errorDiv.className = "bot-msg";
        errorDiv.innerText = "⚠️ Server error. Please try again.";
        chatBox.appendChild(errorDiv);
    });
}

/* ---------------------------------
   Quick Ask Buttons
---------------------------------- */
function quickAsk(question) {
    inputBox.value = question;
    sendMessage();
}

/* ---------------------------------
   Auto-Suggestions While Typing
---------------------------------- */
if (inputBox && suggestionsBox) {
    inputBox.addEventListener("input", () => {
        const text = inputBox.value.toLowerCase();
        suggestionsBox.innerHTML = "";

        if (!text) {
            suggestionsBox.classList.add("hidden");
            return;
        }

        const matches = faqSuggestions.filter(q =>
            q.toLowerCase().includes(text)
        );

        if (matches.length === 0) {
            suggestionsBox.classList.add("hidden");
            return;
        }

        matches.forEach(q => {
            const chip = document.createElement("span");
            chip.innerText = q;
            chip.onclick = () => quickAsk(q);
            suggestionsBox.appendChild(chip);
        });

        suggestionsBox.classList.remove("hidden");
    });
}

/* ---------------------------------
   Emoji Picker Support
---------------------------------- */
function addEmoji(emoji) {
    inputBox.value += emoji;
    inputBox.focus();
}

function addEmoji(emoji) {
    const input = document.getElementById("user-input");
    input.value += emoji;
    input.focus();
}

/* ---------------------------------
   Dark Mode Toggle (ADDED ONLY)
---------------------------------- */
function toggleDarkMode() {
    document.body.classList.toggle("dark");
}
