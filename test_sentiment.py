from sentiment_core import analyze_sentiment

# Ask the user to input text
user_input = input("Enter text to analyze sentiment: ")

# Get sentiment result
result = analyze_sentiment(user_input)

# Print the result
print(f"\nSentiment: {result['label']}")
print(f"Confidence Score: {result['score']:.2f}")
