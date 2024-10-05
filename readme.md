# MemeBuddy: Making memes accessible for the visually impaired.

## Mission Statement
In a world where visual media dominates online interactions, memes and images have become a cultural language of their own. Unfortunately, blind and visually impaired users often find this part of the internet inaccessible, limiting their participation in meme culture. This Chrome extension takes the first step toward making memes more accessible by analyzing screenshots of visual content and providing auditory feedback. With the help of OpenAI’s powerful language model, this extension bridges the gap between text and image-based media, ensuring blind users can enjoy and engage with memes in an inclusive way.

## Files Overview

### 1. `manifest.json`
This file configures the Chrome extension, specifying its permissions and defining key components like the background script and content script. It ensures the extension can capture screenshots, store the API key, and interact with active browser tabs.

### 2. `background.js`
This file is the heart of the extension. It captures screenshots of the active tab, sends the images to OpenAI for analysis, and receives the results. The `background.js` file also communicates with the content script to deliver the analysis results for Text-to-Speech output. Additionally, it handles the storage and retrieval of the OpenAI API key entered by the user in the popup form.

### 3. `contentScript.js`
The content script is injected into the active tab to enable the browser's built-in Text-to-Speech (TTS) functionality. Once the `background.js` sends the analysis from OpenAI, the `contentScript.js` will read the result aloud using TTS, making the content accessible for blind users.

### 4. `popup.html`
This file provides the user interface when the extension icon is clicked in the toolbar. It contains a simple, responsive form where users can enter their OpenAI API key. The form is fully accessible, allowing blind and visually impaired users to navigate it using keyboard shortcuts and screen readers. The entered API key is securely stored in Chrome’s storage.

### 5. `popup.js`
This file manages the interaction within the popup form. It captures the OpenAI API key entered by the user and stores it in Chrome’s storage. The key is then used by `background.js` to send requests to OpenAI when the user captures a screenshot. This file ensures that the user setup process is seamless and keyboard-accessible.

## Accessibility and Screen Reader Instructions

This extension has been designed with accessibility in mind. Here are a few key points for blind users using screen reading software and keyboard navigation:

- **Opening the Extension**: Press `Alt` + `Shift` + `E` to open Chrome’s extension toolbar. Use the arrow keys to navigate to the OpenAI Screenshot extension and press `Enter` to activate it.
- **Entering the OpenAI API Key**: After activating the extension, the popup form will appear. The form is fully keyboard-accessible:
  - Press `Tab` to move focus to the input field.
  - Once in the input field, you can type your OpenAI API key.
  - Press `Tab` again to move to the submit button.
  - Press `Enter` to save the API key.
- **Capturing a Screenshot**: After you’ve entered the API key, the extension will be ready to capture screenshots. You can trigger screenshot capture from the popup or with a keyboard shortcut assigned in Chrome’s extension settings.
- **Hearing the Analysis**: Once the screenshot is captured and analyzed by OpenAI, the extension will read the results aloud using the browser's Text-to-Speech engine. You don’t need to take any extra action to hear the result; it will automatically be spoken after processing.

### Screen Reader Navigation:
- Use the **Tab** key to move between elements in the popup.
- Use **Shift + Tab** to move backward through the form elements.
- Once the form is submitted, the extension operates in the background. Any auditory feedback from the analysis will be read aloud automatically.

### Popup Form Responsiveness:
- The popup form in `popup.html` is responsive, meaning it adjusts to different screen sizes and works well with screen readers. Whether using a keyboard or mouse, blind and visually impaired users can easily navigate and input their OpenAI API key.

## How It Works

1. **User Setup**: After clicking the extension icon, the popup form will open, allowing the user to enter their OpenAI API key.
2. **Screenshot Capture**: Once the key is stored, the extension can capture a screenshot of the active tab. This is done by pressing a designated key or interacting with the popup interface.
3. **API Communication**: The captured image is sent to OpenAI’s API for analysis. The result of the analysis is then sent back to the extension.
4. **Text-to-Speech Output**: The analysis result is read aloud using the browser’s built-in Text-to-Speech (TTS) functionality, ensuring that blind users can hear the content that would otherwise be visual.

## Installation

1. Clone or download the repository.
2. Navigate to `chrome://extensions/` in your Chrome browser.
3. Enable **Developer Mode** in the top-right corner of the screen.
4. Click **Load unpacked** in the top-left corner and select the extension's directory.
5. The extension will now appear in your Chrome toolbar.

## Usage

1. Click the extension icon in the toolbar or use the keyboard to activate the extension with `Alt` + `Shift` + `E`.
2. Enter your OpenAI API key in the form provided in the popup. Use the **Tab** key to navigate between the form fields and the submit button.
3. Use the extension to capture screenshots and receive auditory feedback based on the image analysis.

## Author

Developed by William Hebden.

---

This document has been formatted to ensure accessibility for blind users. The extension is designed with the goal of improving the accessibility of visual content online, starting with memes and image-based media. Through clear navigation and Text-to-Speech integration, this Chrome extension allows blind users to experience visual content in a new, accessible way.