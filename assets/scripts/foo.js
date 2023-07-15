// Select the div element with the class "foo"
const div = document.querySelector('.foo');
  
// Define an array of text options
const texts = ['Text Option 1', 'Text Option 2', 'Text Option 3'];

let currentIndex = 0;

// Function to change the text every second
setInterval(() => {
    div.textContent = texts[currentIndex];
    currentIndex = (currentIndex + 1) % texts.length;
}, 1000);