console.log('Popup script executed.');

document.addEventListener('DOMContentLoaded', function() {
  console.log('DOMContentLoaded event received.');

  document.getElementById('getIdBtn').addEventListener('click', function() {
    // Show "Loading..." message
    document.getElementById('message').innerText = 'Loading...';

    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      var tab = tabs[0];
      var videoId = extractVideoId(tab.url);

      if (videoId) {
        sendMessageToBackground({ action: 'getData', video_id: videoId });
      } else {
        document.getElementById('message').innerText = 'Error: Video ID not found';
      }
    });
  });

  // Function to extract YouTube video ID from URL
  function extractVideoId(url) {
    var match = url.match(/[?&]v=([^&]+)/);
    return match ? match[1] : null;
  }

  // Function to send message to background script
  function sendMessageToBackground(message, callback) {
    chrome.runtime.sendMessage(message, function(response) {
      console.log('Response received:', response);

      if (response && response.message) {
        document.getElementById('message').innerText = response.message;

        // Optionally, update the output container
        if (response.output) {
          document.getElementById('outputContainer').innerText = response.output;
        }
      } else {
        document.getElementById('message').innerText = 'Error: Invalid response';
        console.error('Invalid or missing response:', response);
      }

      if (callback) {
        callback(response);
      }
    });
  }

});
