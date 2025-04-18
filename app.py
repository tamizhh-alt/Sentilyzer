from flask import Flask, render_template, request
from textblob import TextBlob
import nltk

nltk.download('punkt')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Check if 'review' is in the form data to prevent KeyError
    if 'review' not in request.form:
        return "Error: No review provided", 400  # Return an error if the 'review' key is missing

    text = request.form['review']
    
    # If the review is empty, send an error message
    if not text.strip():
        return "Error: Review cannot be empty", 400

    # Perform sentiment analysis using TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    # Determine sentiment
    if sentiment > 0:
        result = "Positive"
    elif sentiment < 0:
        result = "Negative"
    else:
        result = "Neutral"
    
    # Return the result template
    return render_template('result.html', review=text, sentiment=result)

if __name__ == '__main__':
    app.run(debug=True)
