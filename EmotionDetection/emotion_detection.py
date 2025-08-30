"""
Import for json type manipulation and HTTP requests handling
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Function to send a text to the emotion detection API and return results of the analysis
    """
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url = url, headers = headers, json = input_json, timeout=300)

    #Formatting the response
    formatted_response = json.loads(response.text)

    #Extracting emotions scores
    if response.status_code == 200:
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None

    #Building the return value
    dict_emotions_scores = {"anger" : anger_score, "disgust" : disgust_score, "fear" : fear_score, "joy" : joy_score, "sadness" : sadness_score}
    dominant_emotion = None if anger_score is None else max(dict_emotions_scores, key=dict_emotions_scores.get)
    dict_emotions_scores.update({"dominant_emotion" :dominant_emotion})

    return dict_emotions_scores
