"""Flask server for the Emotion Detector application."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Analyze submitted text and return a readable result."""
    text_to_analyze = (
        request.args.get("text", "") if request.method == "GET"
        else request.form.get("text", "")
    )
    if not text_to_analyze.strip():
        return "Please enter a text to analyze.", 400

    try:
        result = emotion_detector(text_to_analyze)
    except (RuntimeError, ValueError) as exc:
        return str(exc), 502

    if result["dominant_emotion"] is None:
        return "Unable to detect emotions for the provided text.", 422

    return (
        "For the given statement, the detected emotions are "
        f"anger: {result['anger']}, disgust: {result['disgust']}, "
        f"fear: {result['fear']}, joy: {result['joy']}, "
        f"sadness: {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
