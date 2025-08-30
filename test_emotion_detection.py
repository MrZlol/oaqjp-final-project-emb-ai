"""
Importing unittest library and the function to test
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Unit testing class for emotion_detector function
    """

    def test_emotion_detector(self):
        """
        Method to run unit tests for emotion_detector function
        """

        #Testing joy emotion detection
        self.assertEqual(emotion_detector("I m glad this happened")["dominant_emotion"], "joy")

        #Testing anger emotion detection
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

        #Testing disgust emotion detection
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")

        #Testing sadness emotion detection
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")

        #Testing fear emotion detection
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()
