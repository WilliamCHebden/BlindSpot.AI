document.addEventListener('DOMContentLoaded', function() {
    // Retrieve stored values when the popup loads
    chrome.storage.sync.get(['openai_api_key', 'prompt'], function(data) {
        if (data.openai_api_key) {
            document.getElementById('openai_api_key').value = data.openai_api_key;
        }
    });
    // Auto-save OpenAI API Key when input changes
    document.getElementById('openai_api_key').addEventListener('input', function() {
        const openaiApiKey = document.getElementById('openai_api_key').value;
        chrome.storage.sync.set({ openai_api_key: openaiApiKey }, function() {
            console.log('OpenAI API Key saved:', openaiApiKey);
        });
    });

});
