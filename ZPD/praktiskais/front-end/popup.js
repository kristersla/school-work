document.addEventListener('DOMContentLoaded', function () {
  console.log('DOMContentLoaded event received.');

  document.getElementById('getIdBtn').addEventListener('click', function () {
    showLoadingScreen();

    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      var tab = tabs[0];
      var videoId = extractVideoId(tab.url);

      if (videoId) {
        sendMessageToBackground({ action: 'getData', video_id: videoId }, function (response) {
          if (response && response.message) {
            document.getElementById('message').innerText = response.message;

            if (response.output) {
              document.getElementById('outputContainer').innerText = response.output;
            }

            if (response.videoTitle) {
              document.getElementById('videoTitle').innerText = `${response.videoTitle}`;
            }

            showResultsSection();
          } else {
            document.getElementById('message').innerText = 'Error: Invalid response';
            console.error('Invalid or missing response:', response);
          }
        });
      } else {
        hideLoadingScreen();
        document.getElementById('message').innerText = 'Error: Video ID not found';
      }
    });
  });

  document.getElementById('getIdBtn2').addEventListener('click', function () {
    shownegativeHeroSection();
  });

  document.getElementById('getIdBtn3').addEventListener('click', function () {
    showneutralHeroSection();
  });

  document.getElementById('getIdBtn4').addEventListener('click', function () {
    showpositiveHeroSection();
  });

  document.getElementById('getIdBtn5').addEventListener('click', function () {
    showHeroSection();
  });

  document.getElementById('getIdBtn6').addEventListener('click', function () {
    showHero2Section();
  });

  document.getElementById('getIdBtn7').addEventListener('click', function () {
    showHero3Section();
  });

  function extractVideoId(url) {
    var match = url.match(/[?&]v=([^&]+)/);
    return match ? match[1] : null;
  }

  function sendMessageToBackground(message, callback) {
    chrome.runtime.sendMessage(message, function (response) {
      console.log('Response received:', response);

      hideLoadingScreen();

      if (response && response.message) {
        document.getElementById('message').innerText = response.message;

        if (response.output) {
          document.getElementById('outputContainer').innerText = response.output;
        }

        showResultsSection();

        if (response && response.negative) {
          document.getElementById('negative').innerText = response.negative;
        } else {
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
    document.querySelector('.hero').style.display = 'none';
    document.querySelector('.results').style.display = 'block';
  }

  function shownegativeHeroSection() {

    document.querySelector('.results').style.display = 'none';
    document.querySelector('.negativeHero').style.display = 'block';
  }

  function showneutralHeroSection() {

    document.querySelector('.results').style.display = 'none';

    document.querySelector('.neutralHero').style.display = 'block';
  }

  function showpositiveHeroSection() {
    document.querySelector('.results').style.display = 'none';

    document.querySelector('.positiveHero').style.display = 'block';
  }

  function showHeroSection() {
    document.querySelector('.negativeHero').style.display = 'none';

    document.querySelector('.results').style.display = 'block';
  }

  function showHero2Section() {
    document.querySelector('.neutralHero').style.display = 'none';

    document.querySelector('.results').style.display = 'block';
  }

  function showHero3Section() {
    document.querySelector('.positiveHero').style.display = 'none';

    document.querySelector('.results').style.display = 'block';
  }


});
