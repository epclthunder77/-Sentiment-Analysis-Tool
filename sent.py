from transformers import pipeline

from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis')

# Array of reviews
reviews = [
    "I love this product! It works great and is easy to use.",
    "This was the worst purchase I've ever made. Terrible quality!",
    "I'm not sure if I like it. It's okay, but could be better."
]

# Analyze and print sentiment for each review
for review in reviews:
    sentiment = sentiment_analyzer(review)
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}\n")
