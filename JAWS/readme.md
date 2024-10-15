# JAWS Integration with Logo_Image_One Browser Extension

This folder contains JAWS scripting examples and instructions for integrating JAWS with the **Logo_Image_One** browser extension. By using the JAWS scripting language (JSL), users can trigger events, such as taking screenshots or analyzing content, directly from the JAWS interface.

## Files in This Folder
- `TriggerScreenshot.jss`: A custom JAWS script that injects a DOM element into the browser to trigger the extension.
- `README.md`: Documentation on how to install and use the JAWS script.
- `ExampleHotkeys.txt`: Suggested key combinations for triggering the extension from JAWS.
  
## How to Use:
1. Install JAWS if you haven't already.
2. Place the `.jss` files in your JAWS `Settings` folder.
3. Load the browser extension, ensuring it listens for DOM changes.
4. Use the configured hotkey (Ctrl + Shift + S) to trigger the screenshot and AI analysis function.
