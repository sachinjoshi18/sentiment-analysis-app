from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Classification
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    
    return sentiment, polarity, subjectivity


@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = ""
    polarity = ""
    subjectivity = ""
    text = ""

    if request.method == 'POST':
        text = request.form['text']
        sentiment, polarity, subjectivity = analyze_sentiment(text)

    return render_template('index.html',
                           sentiment=sentiment,
                           polarity=polarity,
                           subjectivity=subjectivity,
                           text=text)


if __name__ == '__main__':
    app.run(debug=True)