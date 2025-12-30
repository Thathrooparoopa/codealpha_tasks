/************ THEME TOGGLE ************/
(function () {
    const saved = localStorage.getItem("theme");
    if (saved === "light") {
        document.body.classList.add("theme-light");
    } else {
        document.body.classList.add("theme-dark");
    }
})();

document.getElementById("themeToggle").addEventListener("click", () => {
    const dark = document.body.classList.contains("theme-dark");
    document.body.classList.toggle("theme-dark", !dark);
    document.body.classList.toggle("theme-light", dark);
    localStorage.setItem("theme", dark ? "light" : "dark");
});

/************ Loader ************/
function startLoading() {
    document.getElementById("loader").classList.remove("d-none");
}
function stopLoading() {
    document.getElementById("loader").classList.add("d-none");
}

/************ Slider ************/
const slider = document.getElementById("musicLength");
const lengthValue = document.getElementById("lengthValue");
lengthValue.innerText = slider.value;
slider.oninput = () => lengthValue.innerText = slider.value;

/************ Upload ************/
function uploadMidi() {
    const files = document.getElementById("midiFiles").files;
    if (!files.length) {
        document.getElementById("status").innerText = "Select MIDI files first.";
        return;
    }

    const fd = new FormData();
    for (let f of files) fd.append("midi_files", f);

    startLoading();
    fetch("/upload", { method: "POST", body: fd })
        .then(r => r.json())
        .then(d => document.getElementById("status").innerText = d.message || d.error)
        .finally(stopLoading);
}

/************ Train ************/
function trainModel() {
    startLoading();
    document.getElementById("status").innerText = "Training started...";
    fetch("/train", { method: "POST" })
        .then(r => r.json())
        .then(d => document.getElementById("status").innerText = d.message || d.error)
        .finally(stopLoading);
}

/************ Generate ************/
function generateMusic() {
    startLoading();
    fetch("/generate", { method: "POST" })
        .then(r => r.json())
        .then(d => {
            document.getElementById("status").innerText = d.message || d.error;
            if (!d.error) {
                const p = document.getElementById("audioPlayer");
                p.src = "/download";
                p.classList.remove("d-none");
                p.play();
            }
        })
        .finally(stopLoading);
}
