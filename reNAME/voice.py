import os
from transformers import pipeline

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Initialize the pipeline for automatic speech recognition (ASR)
transcriber = pipeline(task="automatic-speech-recognition")

# Define the path to the audio file
audio_path = r"C:\Users\AdminT\Documents\Automation\Automation\reNAME\audio.mp3"

# Transcribe the audio file
try:
    transcription = transcriber(audio_path)
    print(transcription)
except Exception as e:5qw
    print(f"An error occurred: {e}")

