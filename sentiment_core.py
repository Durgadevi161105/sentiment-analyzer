from transformers import pipeline

# Load the sentiment analysis model once
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_model(text)
    return result[0]  # Example: {'label': 'POSITIVE', 'score': 0.998}
