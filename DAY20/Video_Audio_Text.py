# Step 1: Install ffmpeg
!apt-get update
!apt-get install -y ffmpeg

# Step 2: Upload a video file (e.g., .mp4)
from google.colab import files
uploaded = files.upload()

# Step 3: Extract audio from the uploaded video
import os

# Get the uploaded video file name
video_filename = list(uploaded.keys())[0]
audio_filename = "output_audio.wav"  # You can name it anything

# Run ffmpeg command to extract audio
os.system(f"ffmpeg -i '{video_filename}' -vn -acodec pcm_s16le -ar 16000 -ac 1 '{audio_filename}'")

# Step 4: Download the extracted audio
from google.colab import files
files.download(audio_filename) 

# ----------------------------------------------------------------------------------------------------------------------
!pip install git+https://github.com/openai/whisper.git 
import whisper

model = whisper.load_model("base")  # or "small", "medium", "large"
result = model.transcribe("output_audio.wav")
print(result["text"])import whisper

model = whisper.load_model("base")  # or "small", "medium", "large"
result = model.transcribe("output_audio.wav")
print(result["text"])
.# Extract text from the result
transcribed_text = result["text"]

# Save it to a text file
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(transcribed_text)

print("Transcription saved successfully to 'transcription.txt'")
. hi . now i extracted audio from video , and text from audio . now how to give this user friendly . give me idea? 
