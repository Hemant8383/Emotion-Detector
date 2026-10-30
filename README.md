# Emotion Detector

A Flask web application that detects five emotions in English text using the IBM Watson NLP EmotionPredict service.

## Project structure
- `EmotionDetection/emotion_detection.py` — calls the Watson NLP service and formats emotion scores.
- `EmotionDetection/__init__.py` — exposes the `emotion_detector` function.
- `test_emotion_detection.py` — unit tests.
- `server.py` — Flask web application and blank-input handling.
- `templates/index.html` — simple user interface.

## Setup
Python 3.9+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Run tests
```bash
python -m unittest -v
```

## Run the web application
```bash
python server.py
```
Open http://127.0.0.1:5000 in your browser.

## Watson NLP service
The application uses the IBM Skills Network Watson NLP emotion endpoint configured in
`EmotionDetection/emotion_detection.py`. Internet access is required. If the hosted
endpoint is unavailable, the detector raises a clear service error rather than
inventing emotion scores.

## Static analysis
```bash
pip install pylint
pylint server.py EmotionDetection/emotion_detection.py
```
A perfect Pylint score depends on the installed Pylint version and its enabled rules.
