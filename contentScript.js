chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "displayModal") {
    // Read the content aloud using Text-to-Speech
    readAloud(request.content);
    // Respond back to close the message port
    sendResponse({ status: "read aloud" });
  }
});

// Function to read the content aloud
function readAloud(content) {
  if ('speechSynthesis' in window) {
    const utterance = new SpeechSynthesisUtterance(content);
    utterance.rate = 1;  // Set the rate (speed) of speech
    utterance.pitch = 1;  // Set the pitch of the voice
    utterance.lang = 'en-US';  // Set the language
    window.speechSynthesis.speak(utterance);
  } else {
    console.log("Text-to-Speech is not supported in this browser.");
  }
}
