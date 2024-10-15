import pyautogui
import keyboard
import requests
import base64
import pyttsx3
import os
import tkinter as tk
from tkinter import messagebox

# Python script for interacting with the OpenAI API to analyze screenshots of the user's PC and explain it in text-to-speech format that is compatible with JAWS screen reader. To run: Download Python and install the required libraries using pip install pyautogui pyttsx3 keyboard requests. Then, run the script and follow the instructions to enter the OpenAI API key and prompt. The script will listen for the Print Screen key press to capture a screenshot and send it to OpenAI for analysis.

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Global variables to store API key and prompt
openai_api_key = None
prompt = None

# Function to capture screenshot and send to OpenAI for analysis
def capture_and_analyze():
    global openai_api_key, prompt
    
    if not openai_api_key or not prompt:
        print("API key or prompt not found. Please enter both.")
        return

    try:
        # Capture the screenshot
        screenshot = pyautogui.screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)

        # Read the screenshot file as base64
        with open(screenshot_path, "rb") as img_file:
            image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

        # Define the OpenAI API endpoint
        apiUrl = "https://api.openai.com/v1/chat/completions"

        # Prepare the payload with the base64 image and prompt
        payload = {
            "model": "gpt-4-turbo",
            "messages": [
              {
                "role": "user",
                "content": [
                  {
                    "type": "text",
                    "text": prompt
                  },
                  {
                    "type": "image_url",
                    "image_url": {
                      "url": "data:image/png;base64," + image_base64
                    }
                  }
                ]
              }
            ],
            "max_tokens": 500
        }

        # Headers with the OpenAI API key
        headers = {
            "Authorization": f"Bearer {openai_api_key}",
            "Content-Type": "application/json"
        }

        # Send the request to OpenAI
        response = requests.post(apiUrl, json=payload, headers=headers)

        # Process the response from OpenAI
        if response.status_code == 200:
            data = response.json()
            explanation = data['choices'][0]['message']['content']
            print("Explanation from OpenAI:", explanation)

            # Use text-to-speech to read the explanation
            engine.say(explanation)
            engine.runAndWait()
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to handle form submission
def submit_form(api_key_entry, prompt_entry, window):
    global openai_api_key, prompt
    openai_api_key = api_key_entry.get()
    prompt = prompt_entry.get()

    if not openai_api_key or not prompt:
        messagebox.showerror("Error", "Both API key and prompt are required.")
    else:
        messagebox.showinfo("Success", "API key and prompt have been set successfully.")
        window.destroy()  # Close the window after submission

# Function to create the GUI form
def create_form():
    window = tk.Tk()
    window.title("AI Image Explanation App")
    window.geometry("400x300")

    # Label and input for OpenAI API key
    api_key_label = tk.Label(window, text="OpenAI API Key:")
    api_key_label.pack(pady=10)
    api_key_entry = tk.Entry(window, width=50)
    api_key_entry.pack(pady=5)

    # Label and input for the prompt
    prompt_label = tk.Label(window, text="Prompt:")
    prompt_label.pack(pady=10)
    prompt_entry = tk.Entry(window, width=50)
    prompt_entry.pack(pady=5)

    # Submit button
    submit_button = tk.Button(window, text="Submit", command=lambda: submit_form(api_key_entry, prompt_entry, window))
    submit_button.pack(pady=20)

    # Run the Tkinter main loop
    window.mainloop()

# Listen for the Print Screen key press and trigger screenshot capture
def start_listening():
    print("Listening for Print Screen key to capture screenshot...")
    keyboard.add_hotkey('print screen', capture_and_analyze)
    keyboard.wait('esc')  # Exit the script when 'esc' is pressed

# Create the form to enter the OpenAI API key and prompt
create_form()

# Start listening for the Print Screen key press
start_listening()
