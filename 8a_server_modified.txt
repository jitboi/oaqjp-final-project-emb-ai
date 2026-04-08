"""
server.py

This module contains the Flask server application for the Final project.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app : TODO
app=Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response_str = emotion_detector(text_to_analyze)
    dominant_emotion = response_str["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    del response_str["dominant_emotion"]
    # Final response
    response = (
    f"For the given statement, the system response is {response_str}. "
    f"The dominant emotion is {dominant_emotion}."
    )
    return response,200

@app.route("/")
def render_index_page():
    ''' render default index page
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
