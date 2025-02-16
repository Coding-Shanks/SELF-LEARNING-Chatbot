document.addEventListener("DOMContentLoaded", function () {
    const chatWindow = document.getElementById("chat-window");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const teachingSection = document.getElementById("teaching-section");
    const teachInput = document.getElementById("teach-input");
    const teachBtn = document.getElementById("teach-btn");

    // Function to add a message to the chat window
    function addMessage(sender, message) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        messageDiv.innerHTML = `<p>${message}</p>`;
        chatWindow.appendChild(messageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight; // Auto-scroll to the bottom
    }

    // Function to handle user input
    sendBtn.addEventListener("click", function () {
        const message = userInput.value.trim();
        if (message) {
            addMessage("user", message);
            userInput.value = "";

            // Send the message to the backend
            fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: message }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.teach) {
                        teachingSection.style.display = "block"; // Show teaching section
                    } else {
                        addMessage("bot", data.response);
                    }
                });
        }
    });

    // Function to handle teaching the bot
    teachBtn.addEventListener("click", function () {
        const answer = teachInput.value.trim();
        if (answer) {
            fetch("/teach", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    question: chatWindow.lastElementChild.querySelector("p").textContent,
                    answer: answer,
                }),
            })
                .then((response) => response.json())
                .then((data) => {
                    addMessage("bot", data.response);
                    teachingSection.style.display = "none"; // Hide teaching section
                    teachInput.value = "";
                });
        }
    });
});