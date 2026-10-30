from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    text = request.values.get("text", "")

    if not text.strip():
        return "Please enter a text to analyze.", 400

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Emotion analysis service could not process this text.", 400

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
