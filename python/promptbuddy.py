import pyautogui
import keyboard
import openai
import tkinter as tk
from tkinter import simpledialog
import pyaudio
import wave
# This python script allows the user to ask for a screenshot explanation via speech-to text which is sent to the openai api along with the encoded desktop screenshot from the user's computer.

# Initialize OpenAI client 
openai.api_key = api_key_entry.get()

# Function to record audio
def record_audio(filename="recorded_audio.wav"):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = filename

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Function to transcribe audio using OpenAI Whisper
def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcription = openai.Audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    return transcription["text"]

# Function to capture a screenshot and run analysis
def capture_and_analyze(prompt_text):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")

        # OpenAI API call to process the image and prompt
        # You can expand this function with an image analysis function
        print(f"Captured screenshot with prompt: {prompt_text}")
        # Additional logic for sending the screenshot to OpenAI for analysis can be added here.
        
    except Exception as e:
        print(f"Error during screenshot and analysis: {str(e)}")

# Function to handle the prompt input (both text and speech)
def prompt_handler():
    def submit_text_input():
        user_input = simpledialog.askstring("Input", "Enter your prompt:")
        if user_input:
            capture_and_analyze(user_input)

    def submit_speech_input():
        record_audio()  # Record audio from the user
        transcription = transcribe_audio("recorded_audio.wav")  # Transcribe the audio using OpenAI Whisper
        print(f"Transcription: {transcription}")
        capture_and_analyze(transcription)  # Run the analysis with the transcribed text

    # Create a dialog box to ask user for input type
    window = tk.Tk()
    window.withdraw()  # Hide the main window
    input_type = simpledialog.askstring("Input Type", "Type 'text' to type your prompt or 'speech' to speak your prompt:")

    if input_type == "text":
        submit_text_input()
    elif input_type == "speech":
        submit_speech_input()
    else:
        print("Invalid input. Please type 'text' or 'speech'.")

# Bind the hotkey (CTRL + SHIFT + P) to bring up the prompt handler
keyboard.add_hotkey('ctrl+shift+p', prompt_handler)

# Keep the script running to listen for the hotkey
keyboard.wait('esc')  # Press 'esc' to exit the program
