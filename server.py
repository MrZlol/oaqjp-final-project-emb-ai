"""Import flask functions and the local emotion_detector function"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/")
def render_index_page():
    """Rendering the index page"""
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Function to analyze the received text and send back the emotion detection results
    """

    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Creating a string for the return value uisng the (key, value) elements of the response
    dict_to_string = ', '.join(f"'{k}': {v}" for k, v in response.items()\
                         if k != "dominant_emotion")
    dict_to_string = dict_to_string.replace(", 'sadness'", " and 'sadness'")

    return "For the given statement, the system response is " + dict_to_string + \
            ". The dominant emotion is <b>" + response["dominant_emotion"] +"</b>."

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)
