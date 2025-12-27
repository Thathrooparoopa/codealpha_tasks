async function translateText() {
    const text = document.getElementById("inputText").value;
    const source = document.getElementById("sourceLang").value;
    const target = document.getElementById("targetLang").value;
    const error = document.getElementById("error");

    error.innerText = "";

    if (!text.trim()) {
        error.innerText = "Please enter text!";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/translate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text, source, target})
        });

        const data = await response.json();

        if (data.error) {
            error.innerText = data.error;
        } else {
            document.getElementById("outputText").value = data.translatedText;
        }
    } catch {
        error.innerText = "Network error!";
    }
}

function copyText() {
    const output = document.getElementById("outputText");
    output.select();
    document.execCommand("copy");
    alert("Copied!");
}

function speakText() {
    const text = document.getElementById("outputText").value;
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = document.getElementById("targetLang").value;
    speechSynthesis.speak(utterance);
}
// Dark Mode Toggle
function toggleTheme() {
    document.body.classList.toggle("dark");
}

// Swap languages
function swapLanguages() {
    const temp = sourceLang.value;
    sourceLang.value = targetLang.value;
    targetLang.value = temp;
}

// UI wrapper for translate (backend untouched)
async function translateWithUI() {
    const loader = document.getElementById("loader");
    const toast = document.getElementById("toast");

    loader.classList.remove("hidden");

    try {
        await translateText(); // existing backend function
        toast.classList.add("show");
        setTimeout(() => toast.classList.remove("show"), 2000);
    } finally {
        loader.classList.add("hidden");
    }
}
