from flask import Flask, render_template, request, jsonify
import json
from difflib import get_close_matches

app = Flask(__name__)


# Load knowledge base from a JSON file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
        return data


# Save knowledge base to a JSON file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


# Find the best match for the user's question
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


# Get the answer for a specific question from the knowledge base
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Chatbot API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    knowledge_base = load_knowledge_base("knowledge_base.json")

    best_match = find_best_match(
        user_input, [q["question"] for q in knowledge_base["questions"]]
    )
    if best_match:
        answer = get_answer_for_question(best_match, knowledge_base)
        return jsonify({"response": answer})
    else:
        return jsonify({"response": "I don't know. Can you teach me?", "teach": True})


# Teach the bot a new response
@app.route("/teach", methods=["POST"])
def teach():
    user_input = request.json.get("question")
    new_answer = request.json.get("answer")
    knowledge_base = load_knowledge_base("knowledge_base.json")

    knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
    save_knowledge_base("knowledge_base.json", knowledge_base)

    return jsonify({"response": f"Thank you! I learned: {new_answer}"})


if __name__ == "__main__":
    app.run(debug=True)
