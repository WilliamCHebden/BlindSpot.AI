chrome.commands.onCommand.addListener((command) => {
  if (command === "capture-screenshot") {
    console.log("Screenshot command triggered");
    captureAndSendScreenshot();
  }
});

function captureAndSendScreenshot() {
  chrome.storage.sync.get('openai_api_key', function(data) {
    if (data.openai_api_key) {
      const apiKey = data.openai_api_key;  // Use the retrieved API key

      // Capture the visible tab (screenshot)
      chrome.tabs.captureVisibleTab(null, { format: "png" }, (dataUrl) => {
        if (dataUrl) {
          console.log("Screenshot captured");

          // Remove the data URL prefix to get the base64 string
          const imageBase64 = dataUrl.replace(/^data:image\/(png|jpg);base64,/, "");

          // Define the OpenAI API endpoint
          const apiUrl = "https://api.openai.com/v1/chat/completions";

          // Define the prompt to send to OpenAI
          const promptText = "Explain this meme to a blind person. Serach the web if anything is beyond your understanding. If the meme depicts a video game, name the video game featured. If it's a popular meme format, explain about that meme format. If the meme needs to be understood within the context of text written alongside the post, explain that as well."; // Add your prompt text here

          // Prepare the payload with the prompt and base64-encoded image
          const payload = {
            "model": "gpt-4-turbo",
            "messages": [
              {
                "role": "user",
                "content": [
                  {
                    "type": "text",
                    "text": promptText
                  },
                  {
                    "type": "image_url",
                    "image_url": {
                      "url": "data:image/png;base64," + imageBase64
                    }
                  }
                ]
              }
            ],
            "max_tokens": 500
          };

          // Define the headers for the API request, now using the dynamically retrieved API key
          const headers = {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${apiKey}`
          };

          // Send the request to OpenAI API
          fetch(apiUrl, {
            method: "POST",
            headers: headers,
            body: JSON.stringify(payload)
          })
          .then(response => response.json())
          .then(data => {
            console.log("API Response:", data); // Log the API response to the console

            // Save the response using chrome.storage.sync and append it to previous responses
            chrome.storage.sync.get(['responses'], function(result) {
              let responses = result.responses || [];
              responses.push(data);
              chrome.storage.sync.set({ responses: responses }, function() {
                console.log('Response saved:', data);
              });
            });

            // Extract the relevant content from the API response
            const analysisContent = data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content 
              ? data.choices[0].message.content 
              : "No analysis content found";

            // Query the active tab to get the correct tab ID
            chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
              if (chrome.runtime.lastError) {
                console.error("Error querying tabs: ", chrome.runtime.lastError);
              } else if (tabs && tabs[0] && tabs[0].id) {
                // Ensure content script is injected before sending the message
                chrome.scripting.executeScript({
                  target: { tabId: tabs[0].id },
                  files: ['contentScript.js']
                }, () => {
                  if (chrome.runtime.lastError) {
                    console.error("Error injecting script: ", chrome.runtime.lastError);
                  } else {
                    // Send the message without expecting a response
                    chrome.tabs.sendMessage(tabs[0].id, { action: "displayModal", content: analysisContent });
                  }
                });
              } else {
                console.error("No active tab found or tab ID is undefined.");
              }
            });
          })
          .catch(error => {
            console.error("Error in API call:", error);
            // Send an error message to the content script to display in the modal
            chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
              if (tabs && tabs[0] && tabs[0].id) {
                chrome.scripting.executeScript({
                  target: { tabId: tabs[0].id },
                  files: ['contentScript.js']
                }, () => {
                  chrome.tabs.sendMessage(tabs[0].id, { action: "displayModal", content: "API call failed: " + error });
                });
              }
            });
          });
        } else {
          console.error("Failed to capture screenshot");
        }
      });
    } else {
      console.error('No OpenAI API key found in storage.');
    }
  });
}

