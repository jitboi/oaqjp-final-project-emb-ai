import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=headers)
    response_obj  = response.json()
    
    emotionPrediction = response_obj["emotionPredictions"][0]
    anger = emotionPrediction["emotion"]["anger"]
    disgust = emotionPrediction["emotion"]["disgust"]
    fear = emotionPrediction["emotion"]["fear"]
    joy = emotionPrediction["emotion"]["joy"]
    sadness = emotionPrediction["emotion"]["sadness"]
    dominant_emotion = max(emotionPrediction["emotion"], key=emotionPrediction["emotion"].get)
    
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }