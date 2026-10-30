"""Unit tests for the EmotionDetection package."""
import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_returns_formatted_emotions(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01, "disgust": 0.02, "fear": 0.03,
                    "joy": 0.90, "sadness": 0.04
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very happy")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)
        self.assertEqual(set(result), {
            "anger", "disgust", "fear", "joy", "sadness",
            "dominant_emotion"
        })

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_handles_bad_request(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector(" ")
        self.assertIsNone(result["dominant_emotion"])

    def test_handles_blank_input_without_request(self):
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
