# Flask ChatBot

A modern chatbot built with Flask for the backend and HTML/CSS/JavaScript for the frontend. This chatbot can answer questions and learn new responses when it doesn't know the answer. Perfect for beginners and developers looking to build a web-based chatbot.

## 🚀 Live Demo
[Click here to see the live demo](#) *(Add your live demo link once deployed)*

## ✨ Features
- **Real-Time Chat:** Users can interact with the chatbot in real-time.
- **Teach the Bot:** If the bot doesn’t know the answer, users can teach it new responses.
- **JSON Knowledge Base:** All questions and answers are stored in a `knowledge_base.json` file.
- **Responsive Design:** The chat interface is fully responsive and works on all devices.

## 🛠 Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Data Storage:** JSON file (`knowledge_base.json`)

## 📸 Screenshots
*(Add screenshots of your chatbot interface here)*

## ⚙️ Installation
Follow these steps to set up the project locally:

### Clone the Repository:
```bash
git clone https://github.com/your-username/flask-chatbot.git
cd flask-chatbot
```

### Set Up a Virtual Environment (Optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies:
```bash
pip install flask
```

### Run the Application:
```bash
python app.py
```

### Open Your Browser:
Go to **http://127.0.0.1:5000** to see the chatbot in action.

## 📂 Folder Structure
```
flask-chatbot/
│
├── app.py                  # Flask backend
├── templates/              # HTML templates
│   └── index.html          # Main chatbot interface
├── static/                 # Static files (CSS, JS)
│   ├── styles.css          # Custom CSS for styling
│   └── script.js           # JavaScript for interactivity
└── knowledge_base.json     # Knowledge base file
```

## 🔍 How It Works
1. The user types a message in the chat input and clicks "Send".
2. The message is sent to the Flask backend via a **POST request**.
3. The backend checks if the question exists in the `knowledge_base.json` file.
4. If the question exists, the bot responds with the corresponding answer.
5. If the question doesn’t exist, the bot asks the user to teach it the answer.
6. The user can type the answer in the teaching section and click **"Teach"** to save it.

## 🎨 Customization
- **Add More Questions:** Edit the `knowledge_base.json` file to include more questions and answers.
- **Change Styling:** Modify the `static/styles.css` file to customize the chatbot’s look.
- **Deploy Online:** Use platforms like **Heroku, Render, or PythonAnywhere** to deploy your chatbot online.

## 🤝 Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

1. **Fork** the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a **pull request**.

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 👤 Author
**Your Name** *(Replace with your name)*

## ⭐ Support
If you find this project helpful, please give it a **⭐️ on GitHub**!

## 🌐 Connect with Me
- **GitHub:** [github.com/your-username](https://github.com/your-username)
- **LinkedIn:** [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
- **Twitter:** [twitter.com/your-handle](https://twitter.com/your-handle)

## 🏆 Acknowledgments
- **Flask Documentation:** [Flask Official Docs](https://flask.palletsprojects.com/)
- **JavaScript Fetch API:** [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- Inspiration from various chatbot tutorials and projects.

---
This **README.md** provides a clear, structured overview of your chatbot project. Don't forget to replace **your-username** and **Add your live demo link** before publishing! 🚀
