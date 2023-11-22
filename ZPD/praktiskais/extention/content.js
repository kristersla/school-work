// content.js

function showWorkingScreen() {
    // Create a black overlay div
    const overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    overlay.style.color = '#fff';
    overlay.style.display = 'flex';
    overlay.style.justifyContent = 'center';
    overlay.style.alignItems = 'center';
    overlay.innerHTML = '<p>Working...</p>';
  
    // Append the overlay to the body
    document.body.appendChild(overlay);
  
    // Simulate some asynchronous operation (e.g., an API call)
    setTimeout(() => {
      // After the operation is done, remove the overlay
      overlay.remove();
    }, 2000); // Replace 2000 with the actual time your operation takes
  }
  
  // Add an event listener to the button
  document.getElementById('getIdBtn').addEventListener('click', showWorkingScreen);
  