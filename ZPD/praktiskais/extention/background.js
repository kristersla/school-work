console.log('Background script executed.');

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  console.log('Background script received message:', request);

  if (request.action === 'getData') {
    // Send the video ID to the server and let the server handle the message construction
    fetch(`http://localhost:8080/getData?video_id=${request.video_id}`)
      .then(response => response.json())
      .then(data => {
        console.log('Data from Python server:', data);

        // Fetch the video details including the title using the YouTube Data API
        fetch(`https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${request.video_id}&key=AIzaSyBrlZLMhq1thWEuGp6bxQufQka7fUUj9b4`)
          .then(response => response.json())
          .then(videoData => {
            const videoTitle = videoData.items[0]?.snippet?.title || 'Video Title Not Available';

            // Include the video title in the response
            sendResponse({ ...data, videoTitle });
          })
          .catch(error => {
            console.error('Error fetching video details from YouTube API:', error);
            sendResponse({ message: 'Error fetching data' });
          });
      })
      .catch(error => {
        console.error('Error fetching data from Python server:', error);
        sendResponse({ message: 'Error fetching data' });
      });

    return true;
  }
});
