# Install required packages
!pip install -q gradio git+https://github.com/openai/whisper.git ffmpeg-python

import gradio as gr
import whisper
import ffmpeg
import tempfile

# Load Whisper model (you can change "base" to "tiny" or "small" for faster output)
model = whisper.load_model("base")

def transcribe_video(video_file):
    try:
        # Save uploaded video to a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_vid:
            temp_vid.write(video_file)
            temp_vid.flush()
            video_path = temp_vid.name
        print("✅ Video saved:", video_path)

        # Save audio path to another temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as audio_file:
            audio_path = audio_file.name

        # Extract audio using ffmpeg
        ffmpeg.input(video_path).output(audio_path, acodec='pcm_s16le', ac=1, ar='16000').run(overwrite_output=True)
        print("✅ Audio extracted:", audio_path)

        # Transcribe using Whisper
        print("🧠 Transcribing...")
        result = model.transcribe(audio_path)

        return result["text"]

    except Exception as e:
        return f"❌ Error: {str(e)}"

# Gradio interface
gr.Interface(
    fn=transcribe_video,
    inputs=gr.File(type="binary", label="Upload MP4 Video"),
    outputs="text",
    title="🎤 Video to Text Transcriber",
    description="Upload an MP4 video. This app extracts audio and transcribes the speech into text using OpenAI's Whisper. (First run may take time depending on video length)"
).launch()
