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
        return {'dominant_emotion': None}

    response_json = json.loads(response.text)

    ret = response_json['emotionPredictions'][0]['emotion']

    dominant = None
    score = 0
    for key, emotion in ret.items():
        if emotion > score:
            dominant = key
            score = emotion

    ret['dominant_emotion'] = dominant
    return ret
