import json
import os

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

CHART_LABELS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
CHART_VALUES = [12, 19, 8, 15, 22, 30, 25]

MESSAGES_FILE = os.path.join(os.path.dirname(__file__), "messages.json")


def load_messages():
    if not os.path.exists(MESSAGES_FILE):
        return []
    with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_messages(messages):
    with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2)


@app.route("/")
def index():
    return render_template(
        "index.html",
        chart_labels=json.dumps(CHART_LABELS),
        chart_values=json.dumps(CHART_VALUES),
        messages=load_messages(),
    )


@app.route("/say-hi", methods=["POST"])
def say_hi():
    name = request.form.get("name", "").strip()
    message = request.form.get("message", "").strip()
    if name and message:
        messages = load_messages()
        messages.append({"name": name, "message": message, "reply": ""})
        save_messages(messages)
    return redirect(url_for("index"))


@app.route("/reply/<int:index>", methods=["POST"])
def reply(index):
    reply_text = request.form.get("reply", "").strip()
    messages = load_messages()
    if 0 <= index < len(messages) and reply_text:
        messages[index]["reply"] = reply_text
        save_messages(messages)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
