import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.metrics.distance import jaccard_distance
import string

# Download NLTK data
nltk.download('punkt_tab')   # Required
nltk.download('stopwords')   # Required
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def compute_jaccard_similarity(text1, text2, n=3):
    tokens1 = preprocess(text1)
    tokens2 = preprocess(text2)
    
    ngrams1 = set(ngrams(tokens1, n))
    ngrams2 = set(ngrams(tokens2, n))
    
    if not ngrams1 or not ngrams2:
        return 0.0
    
    similarity = 1 - jaccard_distance(ngrams1, ngrams2)
    return similarity

def check_plagiarism(text1, text2, threshold=0.5):
    similarity = compute_jaccard_similarity(text1, text2)
    print(f"Jaccard Similarity: {similarity:.2f}")
    if similarity >= threshold:
        print("❗ Potential Plagiarism Detected!")
    else:
        print("✅ Texts are mostly original.")

# Example
text1 = "Natural Language Processing is a subfield of AI."
text2 = "AI includes many areas such as Natural Language Processing."

check_plagiarism(text1, text2)
