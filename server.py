"""
Running this file will start a flask server on port 5000
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create the flask app
app = Flask("Emotion Analyser")

@app.route("/")
def render_index_page():
    """
    The homepage 
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_analyzer():
    # Response message
    message = "For the given statement, the system response is "
    # get the text entered
    text_to_analyze = request.args.get('textToAnalyze')
    # Analyze the text
    response = emotion_detector(text_to_analyze)
    # Build the final message to be displayed
    #message += response + dominant_str
    message += "'anger': " + str(response['anger']) + ', '
    message += "'disgust': " + str(response['disgust']) + ', '
    message += "'fear': " + str(response['fear']) + ', '
    message += "'joy': " + str(response['joy']) + ', '
    message += "'sadness': " + str(response['sadness']) + '. '
    message += "The dominant emotion is " + response['dominant_emotion']
    return message    

# Run the flask app on localhost port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)