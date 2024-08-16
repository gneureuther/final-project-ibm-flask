"""
A unit test for the emotion_detector
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class UnittestEmotion(unittest.TestCase):
    """
    A class that will test Dominant Emotions 
    """
    def test_emotion(self):
        """
        A function to test each for Dominant emotions
        """
        # joy
        test_joy = emotion_detector("I am glad this happened")
        self.assertEqual(test_joy['dominant_emotion'], 'joy')
        # anger
        test_anger = emotion_detector("I am really mad about this")
        self.assertEqual(test_anger['dominant_emotion'], 'anger')
        # disgust
        test_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_disgust['dominant_emotion'], 'disgust')
        # sadness
        test_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(test_sadness['dominant_emotion'], 'sadness')
        # fear
        test_fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test_fear['dominant_emotion'], 'fear')
unittest.main()
