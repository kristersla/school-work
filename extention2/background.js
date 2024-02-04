console.log('Background script executed.');

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  console.log('Background script received message:', request);

  if (request.action === 'getData') {
    fetch(`https://7cb5-141-145-192-62.ngrok-free.app/get_data?video_id=${request.video_id}`)
      .then(response => response.json())
      .then(data => {
        console.log('Data from Python server:', data);

        fetch(`https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${request.video_id}&key=YOUR_YOUTUBE_API_KEY`)
        .then(response => response.json())
        .then(videoData => {
          const videoTitle = videoData.items[0]?.snippet?.title || 'Video Title Not Available';
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
