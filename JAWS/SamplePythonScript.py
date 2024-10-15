import pyautogui
import requests
import base64
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to capture screenshot and analyze it using OpenAI
def capture_and_analyze(api_key, prompt):
    try:
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)

        # Convert image to base64
        with open(screenshot_path, "rb") as img_file:
            image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

        # Send request to OpenAI
        apiUrl = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        payload = {
            "model": "gpt-4-turbo",
            "messages": [
                {"role": "user", "content": [{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": "data:image/png;base64," + image_base64}}]}
            ],
            "max_tokens": 500
        }

        response = requests.post(apiUrl, json=payload, headers=headers)
        if response.status_code == 200:
            explanation = response.json()['choices'][0]['message']['content']
            engine.say(explanation)
            engine.runAndWait()
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example call to the function
api_key = "your-openai-api-key"
prompt = "Please describe the content of this screenshot."
capture_and_analyze(api_key, prompt)
