import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyze):
    result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return result

    try:
        response = requests.post(
            URL,
            headers=HEADERS,
            json={"raw_document": {"text": text_to_analyze}},
            timeout=30
        )

        if response.status_code == 400:
            return result

        response.raise_for_status()
        emotions = response.json()["emotionPredictions"][0]["emotion"]

        for emotion in ["anger", "disgust", "fear", "joy", "sadness"]:
            result[emotion] = emotions[emotion]

        result["dominant_emotion"] = max(
            ["anger", "disgust", "fear", "joy", "sadness"],
            key=lambda emotion: result[emotion]
        )
        return result

    except (requests.RequestException, KeyError, IndexError, ValueError, TypeError):
        return result
