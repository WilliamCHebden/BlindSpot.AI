# JAWS and Logo_Image_One Extension Integration Guide

This guide explains how to use the JAWS script (`TriggerScreenshot.jss`) to interact with the Logo_Image_One browser extension. The JAWS script injects a hidden DOM element that the extension listens for. When the element is detected, the extension captures a screenshot or runs AI analysis to describe on-screen content.

## Steps for Integration:
1. **Install the JAWS Script**: Copy the `TriggerScreenshot.jss` script into your JAWS settings folder.
2. **Set the Hotkey**: By default, the hotkey `Ctrl + Shift + S` is used to trigger the screenshot. Modify the `KeyPressedEvent` in the script if you want to change the key binding.
3. **Activate the Browser Extension**: Ensure the Logo_Image_One extension is running in Chrome or Firefox. The extension is designed to listen for DOM changes, including the hidden `#triggerLogoImageOne` element.
4. **Using the Hotkey**: Press `Ctrl + Shift + S` in your browser while JAWS is running. This will inject a trigger that the browser extension will detect and act upon.
5. **Results**: The browser extension will capture the visible tab and perform AI-based analysis. The analysis results will be read aloud using your browser’s Text-to-Speech engine.

## Troubleshooting:
- Ensure that both JAWS and the browser extension are active.
- Check the console logs in the browser’s developer tools for any issues related to DOM manipulation.
