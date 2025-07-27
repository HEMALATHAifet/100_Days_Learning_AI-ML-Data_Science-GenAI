## 📄 Plagiarism Checker (Basic) – NLTK Based

This is a simple plagiarism checker written in Python that compares two input texts using **Jaccard Similarity** on **n-grams** after removing stopwords and punctuation.

---

### ✨ Features

* Uses **NLTK** for:

  * Tokenization
  * Stopword removal
  * n-gram generation
  * Jaccard distance
* Preprocessing includes:

  * Lowercasing
  * Punctuation removal
  * Stopword removal
* Detects high textual overlap between two documents or strings.

---

### 🔧 Requirements

Install required libraries:

```bash
pip install nltk
```

Download NLTK data resources:

```python
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
```

---

### 🚀 Usage

```python
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.metrics.distance import jaccard_distance
import string

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
    return 1 - jaccard_distance(ngrams1, ngrams2)

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
```

---

### 📌 Sample Output

```
Jaccard Similarity: 0.60
❗ Potential Plagiarism Detected!
```

---

### 📚 How it Works

1. **Text Preprocessing**: Lowercasing, punctuation and stopword removal.
2. **n-gram Generation**: Default `n=3`.
3. **Similarity Calculation**: Jaccard similarity = `1 - jaccard_distance`.
4. **Plagiarism Check**: If similarity ≥ threshold (default 0.5), it's flagged.

---

### 📈 Future Improvements

* Compare uploaded files (PDF, DOCX)
* Check against web sources (with Copyleaks or Turnitin API)
* Add Gradio interface
* Use TF-IDF or BERT embeddings for advanced comparison

---


