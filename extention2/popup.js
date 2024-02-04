document.addEventListener("DOMContentLoaded", function () {
  const readButton = document.getElementById("readButton");
  const positiveButton = document.getElementById("getIdBtn4");
  const negativeButton = document.getElementById("getIdBtn2");
  const neutralButton = document.getElementById("getIdBtn3");

  const outputDiv = document.getElementById("output");
  const negDiv = document.getElementById("negative");
  const neuDiv = document.getElementById("neutral");
  const posDiv = document.getElementById("positive");

  const loadingContainer = document.getElementById("loadingContainer");
  const resultsSection = document.querySelector(".results");
  const negativeHeroSection = document.querySelector(".negativeHero");
  const neutralHeroSection = document.querySelector(".neutralHero");
  const positiveHeroSection = document.querySelector(".positiveHero");

  let loading = false;

  readButton.addEventListener("click", function () {
      if (!loading) {
          setLoading(true);

          chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
              const tab = tabs[0];
              const url = tab.url;

          
              const videoId = extractVideoIdFromUrl(url);

              if (videoId) {
              
                  displayMessage(videoId);
              } else {
                  setLoading(false);
                  outputDiv.innerText = "Could not find YouTube video ID on this page.";
              }
          });
      }
  });

  positiveButton.addEventListener("click", function () {

      showpositiveHeroSection();
  });

  negativeButton.addEventListener("click", function () {

      shownegativeHeroSection();
  });

  neutralButton.addEventListener("click", function () {
 
      showneutralHeroSection();
  });

  function extractVideoIdFromUrl(url) {
      const videoIdMatch = url.match(/(?:youtu\.be\/|youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=))([^"&?\/\s]{11})/);
      return videoIdMatch ? videoIdMatch[1] : null;
  }

  function setLoading(isLoading) {
      loading = isLoading;
      loadingContainer.style.display = isLoading ? "block" : "none";
      resultsSection.style.display = isLoading ? "none" : "block";
      const heroSection = document.querySelector(".hero");
      const loadingSc = document.querySelector(".loadingSc");
      loadingSc.style.display = isLoading ? "block" : "none";

      if (isLoading) {
          heroSection.style.display = "none";
      }
  }

    function displayMessage(videoId) {
        const apiUrl = `https://7cb5-141-145-192-62.ngrok-free.app/get_data?video_id=${videoId}`;

        
        fetch(apiUrl, {
            headers: {
                'ngrok-skip-browser-warning': 'true'
            }
        })
            .then(response => response.json())
            .then(data => {

                const message = data.message;
                outputDiv.innerText = message;

                const negative = data.negative;
                negDiv.innerText = negative;

                const neutral = data.neutral;
                neuDiv.innerText = neutral;

                const positive = data.positive;
                posDiv.innerText = positive;

      
                fetch(`https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=AIzaSyBrlZLMhq1thWEuGp6bxQufQka7fUUj9b4`)
                    .then(response => response.json())
                    .then(videoData => {

                        const videoTitle = videoData.items[0].snippet.title;

   
                        document.getElementById("videoTitle").innerText = videoTitle;
                    })
                    .catch(error => {
                        console.error('Error fetching video details from YouTube API:', error);
                    })
                    .finally(() => {
  
                        setLoading(false);
                    });
            })
            .catch(error => {
                console.error("Error fetching API:", error);
                setLoading(false);
                outputDiv.innerText = "Error fetching API. Please try again later.";
            });
    }

  function shownegativeHeroSection() {

      negativeHeroSection.style.display = 'block';
      resultsSection.style.display = 'none';
  }

  function showneutralHeroSection() {

      neutralHeroSection.style.display = 'block';
      resultsSection.style.display = 'none';
  }

  function showpositiveHeroSection() {

      positiveHeroSection.style.display = 'block';
      resultsSection.style.display = 'none';
  }

  function showHeroSection() {

      negativeHeroSection.style.display = 'none';
      neutralHeroSection.style.display = 'none';
      positiveHeroSection.style.display = 'none';

      resultsSection.style.display = 'block';
  }

  document.getElementById('getIdBtn5').addEventListener('click', function () {

      showHeroSection();
  });

  document.getElementById('getIdBtn6').addEventListener('click', function () {

      showHeroSection();
  });

  document.getElementById('getIdBtn7').addEventListener('click', function () {

      showHeroSection();
  });

});
