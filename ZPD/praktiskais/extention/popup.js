document.addEventListener('DOMContentLoaded', function () {
    var extractButton = document.getElementById('extractButton');
    var sendButton = document.getElementById('sendButton');
    var resultElement = document.getElementById('result');
    var inputDataElement = document.getElementById('inputData');
  
    // Extract YouTube Video ID
    extractButton.addEventListener('click', function () {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var url = tabs[0].url;
        var videoId = extractYouTubeVideoId(url);
        resultElement.textContent = 'YouTube Video ID: ' + videoId;
  
        // Send the YouTube Video ID to localhost
        sendDataToServer(videoId);
      });
    });
  
    // Send data to localhost
    sendButton.addEventListener('click', function () {
      var inputData = inputDataElement.value;
      sendDataToServer(inputData);
    });
  
    function extractYouTubeVideoId(url) {
      var regex = /[?&]v=([^?&]+)/;
      var match = url.match(regex);
      return match && match[1] ? match[1] : null;
    }
  
    function sendDataToServer(data) {
      fetch('http://localhost:5000/process', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: data })
      })
        .then(response => response.json())
        .then(data => {
          resultElement.innerText = 'Result: ' + data.result;
        })
        .catch(error => console.error('Error:', error));
    }
  });
  