# Install NLTK (if not installed)
!pip install nltk
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# Sample text
text = "I absolutely love this product! It's fantastic and worth every penny."

# Get sentiment scores
score = sia.polarity_scores(text)
print(score)
