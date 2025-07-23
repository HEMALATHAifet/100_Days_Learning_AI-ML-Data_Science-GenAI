!pip install -q gradio git+https://github.com/openai/whisper.git ffmpeg-python openai

import gradio as gr
import whisper
import ffmpeg
import tempfile
import openai

# Set your OpenAI API key
openai.api_key = "sk-..."  # ← Replace with your actual key

# Load Whisper model
model = whisper.load_model("base")

# Global variable to hold transcript
global_transcript = ""

def transcribe_video(video_file):
    global global_transcript

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_vid:
            temp_vid.write(video_file)
            temp_vid.flush()
            video_path = temp_vid.name
        print("✅ Video saved:", video_path)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as audio_file:
            audio_path = audio_file.name

        ffmpeg.input(video_path).output(audio_path, acodec='pcm_s16le', ac=1, ar='16000').run(overwrite_output=True)
        print("✅ Audio extracted:", audio_path)

        print("🧠 Transcribing...")
        result = model.transcribe(audio_path)
        transcribed_text = result["text"]
        global_transcript = transcribed_text

        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as text_file:
            text_file.write(transcribed_text)
            text_file_path = text_file.name

        print("✅ Transcription saved to:", text_file_path)
        return transcribed_text, text_file_path

    except Exception as e:
        return f"❌ Error: {str(e)}", None

# Q&A function using OpenAI
def answer_question(user_question):
    if not global_transcript:
        return "⚠️ Please upload and transcribe a video first."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that answers questions based on a given video transcript."},
                {"role": "user", "content": f"Transcript: {global_transcript}"},
                {"role": "user", "content": f"Question: {user_question}"}
            ],
            temperature=0.2,
            max_tokens=300
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"❌ Error calling OpenAI API: {str(e)}"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("🎤 **Video to Text Q&A Assistant**\n\n1. Upload MP4 video\n2. Ask questions based on what was said in the video")

    with gr.Row():
        video_input = gr.File(label="Upload MP4 Video", type="binary")
        transcript_output = gr.Textbox(label="Transcribed Text", lines=10)
        file_output = gr.File(label="Download Transcript")

    transcribe_button = gr.Button("Transcribe Video")
    transcribe_button.click(fn=transcribe_video, inputs=video_input, outputs=[transcript_output, file_output])

    with gr.Row():
        question_input = gr.Textbox(label="Ask a question about the video")
        answer_output = gr.Textbox(label="Answer")

    ask_button = gr.Button("Get Answer")
    ask_button.click(fn=answer_question, inputs=question_input, outputs=answer_output)

demo.launch()
