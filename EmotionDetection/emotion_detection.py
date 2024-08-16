"""
The code calls IBM watson for sentiment analysis of a string.
"""
import json
import requests  # Import the requests library to handle HTTP requests

# IBM Watson url and headers
URL = 'https://sn-watson-emotion.labs.skills.network/'
URL += 'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    """
    Make a api call to analyze the text_to_analyse string.
    """
    obj_doc = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = obj_doc, headers=HEADERS, timeout=10 )
    formatted_text = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_text['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        emotion_indexes = [anger, disgust, fear, joy, sadness]
        # Find the largest emotion index
        dominant_index = max(emotion_indexes)

        # Set the dominant emotion by looping though the dictionary of emotions
        dominant_emotion = ''
        for key, value in emotions.items():
            if value == dominant_index:
                dominant_emotion = key
                break
        # Return the json of the emotion data
        return {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness,
                "dominant_emotion": dominant_emotion }
    return None
