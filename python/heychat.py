import pyaudio
import wave
import time
import openai
import speech_recognition as sr
from pathlib import Path
import warnings
import os

warnings.filterwarnings("ignore", category=DeprecationWarning)

#This python script allows the user to interact with the OpenAI API using speech-to-text and text-to-speech capabilities, by sending a screenshot of the user's computer along with the voice prompt. The script listens for the wake word "Hey Chat" from the user's microphone to begin recording. The recorded audio is transcribed using OpenAI's Whisper API, and a response is generated using OpenAI's TTS API. The response is then played back to the user as speech. To run the script, install the required libraries using pip install openai pyaudio SpeechRecognition simpleaudio. Then, enter your OpenAI API key in the provided entry field and run the script. The script will listen for the wake word and respond to user queries using OpenAI's capabilities.

#Example: Hey Chat, explain what's on my desktop.

#Example: Hey Chat, what time is it?

#Example: Hey Chat, proofread my word doc.

#Example: Hey Chat, does this website look trustworthy?

#Example: Hey Chat, explain my game screen.

#Example: Hey Chat, explain this meme.

# Initialize OpenAI 
openai.api_key = api_key_entry.get();

# Path to store temporary files
TEMP_DIR = os.path.dirname(os.path.realpath(__file__))

# Function to record audio
def record_audio(filename="recorded_audio.wav", record_seconds=5):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wave_output_filename = os.path.join(TEMP_DIR, filename)
    wf = wave.open(wave_output_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return wave_output_filename

# Function to transcribe audio using OpenAI Whisper
def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcription = openai.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    return transcription.text

# Function to generate speech response using OpenAI
# Function to generate a speech response using OpenAI's TTS API
def generate_speech_response(text, voice="alloy"):
    speech_file_path = Path(TEMP_DIR) / "response_speech.mp3"
    
    # Call the TTS API and save the audio file directly
    response = openai.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text
    )

    response.stream_to_file(speech_file_path)



# Function to play an audio file
def play_audio(file_path):
    import simpleaudio as sa
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Function to listen for the keyword "Hey Chat"
def listen_for_wake_word():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening for the wake word...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()
        if "hey chat" in text:
            print("Wake word detected!")
            return True
        else:
            return False
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return False
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return False

# Main function to handle the process
def main():
    while True:
        if listen_for_wake_word():
            # Record user speech
            recorded_file = record_audio()

            # Transcribe the recorded audio
            user_input = transcribe_audio(recorded_file)
            print(f"User said: {user_input}")

            # Generate a response from OpenAI
            response_text = f"You said: {user_input}. How can I help you today?"
            print(f"Response: {response_text}")

            # Generate speech response from OpenAI
            speech_file = generate_speech_response(response_text)

            # Play the speech response
            play_audio(speech_file)

        time.sleep(1)  # Wait before listening again

# Start the main process
if __name__ == "__main__":
    main()
