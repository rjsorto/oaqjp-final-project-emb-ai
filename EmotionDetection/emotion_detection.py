"""
Emotion detection Library
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Querying the Watson API and formating the response
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = obj, headers = headers, timeout = 5)

    if response.status_code == 400:
        return {'dominant_emotion': None}, 400

    response_json = json.loads(response.text)

    formatted_response = response_json['emotionPredictions'][0]['emotion']

    dominant_emotion = max(formatted_response, key = lambda x: formatted_response[x])

    formatted_response['dominant_emotion'] = dominant_emotion

    return formatted_response
