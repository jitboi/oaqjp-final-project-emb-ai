from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app : TODO
app=Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO
    text_to_analyze = request.args.get("textToAnalyze")
    response_str = emotion_detector(text_to_analyze)
    dominant_emotion = response_str["dominant_emotion"]
    del response_str["dominant_emotion"]
    # Final response
    response = (
    f"For the given statement, the system response is {response_str}. "
    f"The dominant emotion is {dominant_emotion}."
    )
    return response,200

@app.route("/")
def render_index_page():
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
