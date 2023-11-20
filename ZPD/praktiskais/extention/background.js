console.log('Background script executed.');

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  console.log('Background script received message:', request);

  if (request.action === 'getData') {
    // Send the video ID to the server and let the server handle the message construction
    fetch(`http://localhost:8080/getData?video_id=${request.video_id}`)
      .then(response => response.json())
      .then(data => {
        console.log('Data from Python server:', data);
        sendResponse(data);
      })
      .catch(error => {
        console.error('Error fetching data from Python server:', error);
        sendResponse({ message: 'Error fetching data' });
      });

    return true;  // Indicates that the sendResponse will be called asynchronously
  }
});
