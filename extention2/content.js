function extractVideoId() {
  const url = window.location.href;
  const videoIdMatch = url.match(/(?:youtu\.be\/|youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=))([^"&?\/\s]{11})/);
  return videoIdMatch ? videoIdMatch[1] : null;
}

function displayApiOutput(videoId) {
  const apiUrl = `https://7cb5-141-145-192-62.ngrok-free.app/get_data?video_id=${videoId}`;
  // Adding the ngrok-skip-browser-warning header
  const fetchOptions = {
    headers: {
      'ngrok-skip-browser-warning': 'true'
    }
  };

  fetch(apiUrl, fetchOptions)
    .then(response => response.json())
    .then(data => {
      const message = data.message;
      const videoTitle = data.videoTitle;

      outputDiv.innerText = message;

      const videoTitleElement = document.getElementById("videoTitleText");
      if (videoTitleElement) {
        videoTitleElement.innerText = videoTitle;
      }

      const negative = data.negative;
      negDiv.innerText = negative;

      const neutral = data.neutral;
      neuDiv.innerText = neutral;

      const positive = data.positive;
      posDiv.innerText = positive;

      setLoading(false);
    })
    .catch(error => {
      console.error("Error fetching API:", error);
      setLoading(false);
      outputDiv.innerText = "Error fetching API. Please try again later.";
    });
}

function addButton() {
  const button = document.createElement("button");
  button.innerText = "Read";
  button.addEventListener("click", () => {
    const videoId = extractVideoId();
    if (videoId) {
      displayApiOutput(videoId);
    } else {
      alert("Could not find YouTube video ID on this page.");
    }
  });

  document.body.appendChild(button);
}

document.addEventListener("DOMContentLoaded", addButton);
