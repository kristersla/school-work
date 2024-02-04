document.addEventListener('DOMContentLoaded', function () {

    var timerElement = document.getElementById('timer');
    var seconds = 0;

    var timerInterval = setInterval(function () {
        seconds++;
        timerElement.innerText = seconds;
    }, 1000);

});
