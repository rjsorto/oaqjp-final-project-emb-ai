from EmotionDetection.emotion_detection import emotion_detection
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        res1 = emotion_detection('I am glad this happened')
        self.assertEqual(res1['dominant_emotion'], 'joy')
        
        res2 = emotion_detection('I am really mad about this')
        self.assertEqual(res2['dominant_emotion'], 'anger')
        
        res3 = emotion_detection('I feel disgusted just hearing about this')
        self.assertEqual(res3['dominant_emotion'], 'disgust')
        
        res4 = emotion_detection('I am so sad about this')
        self.assertEqual(res4['dominant_emotion'], 'sadness')
        
        res4 = emotion_detection('I am really afraid that this will happen')
        self.assertEqual(res4['dominant_emotion'], 'fear')

        # data = [
        #     ['I am glad this happened', 'joy'],
        #     ['I am really mad about this', 'anger'],
        #     ['I feel disgusted just hearing about this', 'disgust'],
        #     ['I am so sad about this', 'sadness'],
        #     ['I am really afraid that this will happen', 'fear']
        # ]

        # for test in data:
        #     res = emotion_detection(test[0])
        #     self.assertEqual(res['dominant_emotion'], test[1])

unittest.main()
