from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detection

app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analize = request.args.get('textToAnalyze')

    response = emotion_detection(text_to_analize)

    if not response: return 'Please check the input and try again'

    return f'From the given statement, the system response is: anger: {response["anger"]}, disgust: {response["disgust"]}, fear: {response["fear"]}, joy: {response["joy"]} and sadness: {response["sadness"]}.<br>The dominant emotion is <b>{response["dominant_emotion"].upper()}.</b>'

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
