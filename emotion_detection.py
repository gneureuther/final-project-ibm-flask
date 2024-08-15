"""
The code calls IBM watson for sentiment analysis of a string.
"""
import json
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    """
    Make a api call to analyze the text_to_analse string.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj_doc = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = obj_doc, headers=headers, timeout=10 )
    formatted_text = json.loads(response.text)
    if response.status_code == 200:
       emotions = formatted_text['emotionPredictions'][0]['emotion']
       anger = emotions['anger']
       disgust = emotions['disgust']
       fear = emotions['fear']
       joy = emotions['joy']
       sadness = emotions['sadness']
       dominant_index = max([anger, disgust, fear, joy, sadness])
       dominant_emotion = 
       return emotions
       #return {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness,
       #         "dominant_emotion:": dominant_emotion }
    return None
    
        