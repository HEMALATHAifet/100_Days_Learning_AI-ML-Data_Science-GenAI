!pip install scikit-learn gradio
import gradio as gr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_plagiarism_tfidf(text1, text2, threshold=0.5):
    if not text1.strip() or not text2.strip():
        return "⚠️ Please provide both texts to compare."

    # Vectorize texts using TF-IDF
    vectorizer = TfidfVectorizer().fit([text1, text2])
    vectors = vectorizer.transform([text1, text2])

    # Compute cosine similarity
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    # Build report
    report = f"🔍 **Cosine Similarity Score:** {similarity:.2f}\n\n"
    if similarity >= threshold:
        report += "❗ **Potential Plagiarism Detected!**"
    else:
        report += "✅ **Texts are mostly original.**"

    return report

# Gradio Interface
interface = gr.Interface(
    fn=check_plagiarism_tfidf,
    inputs=[
        gr.Textbox(label="Text 1", lines=8, placeholder="Paste the first document here..."),
        gr.Textbox(label="Text 2", lines=8, placeholder="Paste the second document here..."),
        gr.Slider(0.0, 1.0, step=0.01, value=0.5, label="Similarity Threshold")
    ],
    outputs=gr.Markdown(),
    title="Plagiarism Checker (TF-IDF Based)",
    description="Compare two texts using Cosine Similarity of TF-IDF vectors. Detects semantic and paraphrased similarity better than n-grams.",
)

interface.launch()
