console.log('Popup script executed.');

document.addEventListener('DOMContentLoaded', function () {
  console.log('DOMContentLoaded event received.');

  document.getElementById('getIdBtn').addEventListener('click', function () {
    // Show loading screen
    showLoadingScreen();

    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      var tab = tabs[0];
      var videoId = extractVideoId(tab.url);

      if (videoId) {
        sendMessageToBackground({ action: 'getData', video_id: videoId });
      } else {
        hideLoadingScreen(); // Hide loading screen in case of an error
        document.getElementById('message').innerText = 'Error: Video ID not found';
      }
    });
  });

  document.getElementById('getIdBtn2').addEventListener('click', function () {
    // Optionally, update negative here
    // No need to set a default message here, it will be updated based on the server response
    shownegativeHeroSection();
  });

  document.getElementById('getIdBtn3').addEventListener('click', function () {
    // No need to set a default message here, it will be updated based on the server response
    showneutralHeroSection();
  });

  document.getElementById('getIdBtn4').addEventListener('click', function () {
    // No need to set a default message here, it will be updated based on the server response
    showpositiveHeroSection();
  });

  function extractVideoId(url) {
    var match = url.match(/[?&]v=([^&]+)/);
    return match ? match[1] : null;
  }

  function sendMessageToBackground(message, callback) {
    chrome.runtime.sendMessage(message, function (response) {
      console.log('Response received:', response);

      // Hide loading screen regardless of the response
      hideLoadingScreen();

      if (response && response.message) {
        document.getElementById('message').innerText = response.message;

        // Optionally, update the output container
        if (response.output) {
          document.getElementById('outputContainer').innerText = response.output;
        }

        // Show the results section
        showResultsSection();

        if (response && response.negative) {
          // Update the negative content here
          document.getElementById('negative').innerText = response.negative;
        } else {
          // Handle the case when negative is not present
          console.error('Error: Invalid or missing negative in the response');
        }

        if (response && response.neutral) {
          document.getElementById('neutral').innerText = response.neutral;
        } else {
          console.error('Error: Invalid or missing neutral in the response');
        }

        if (response && response.positive) {
          document.getElementById('positive').innerText = response.positive;
        } else {
          console.error('Error: Invalid or missing positive in the response');
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

  function showLoadingScreen() {
    document.getElementById('loadingContainer').style.display = 'flex';
  }

  function hideLoadingScreen() {
    document.getElementById('loadingContainer').style.display = 'none';
  }

  function showResultsSection() {
    // Hide the first section
    document.querySelector('.hero').style.display = 'none';

    // Show the results section
    document.querySelector('.results').style.display = 'block';
  }

  function shownegativeHeroSection() {
    // Hide the results section
    document.querySelector('.results').style.display = 'none';

    // Show the negativeHero section
    document.querySelector('.negativeHero').style.display = 'block';
  }

  function showneutralHeroSection() {
    // Hide the results section
    document.querySelector('.results').style.display = 'none';

    document.querySelector('.neutralHero').style.display = 'block';
  }

  function showpositiveHeroSection() {
    // Hide the results section
    document.querySelector('.results').style.display = 'none';

    document.querySelector('.positiveHero').style.display = 'block';
  }


});
