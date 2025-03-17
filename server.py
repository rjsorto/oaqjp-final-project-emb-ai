"""
server module
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detection

app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def emotion_detector():
    """
    Sends the text to be analyzed and formats the response
    """
    text_to_analize = request.args.get('textToAnalyze')

    response = emotion_detection(text_to_analize)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.', 400

    ret = 'From the given statement, the system response is: '
    ret += f'anger: {response["anger"]}, disgust: {response["disgust"]}, '
    ret += f'fear: {response["fear"]}, joy: {response["joy"]} and sadness: {response["sadness"]}.'
    ret += f'<br>The dominant emotion is <b>{response["dominant_emotion"].upper()}.</b>'

    return ret

@app.route('/')
def render_index_page():
    """
    Renders the index.html page
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
