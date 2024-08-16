"""
Running this file will start a flask server on port 5000
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Response message
MESSAGE = "For the given statement, the system response is "

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
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return {MESSAGE: response}    

# Run the flask app on localhost port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)