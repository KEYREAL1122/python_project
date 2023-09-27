// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
  // Add your JavaScript code here
  
  // Example: Perform an action when a button is clicked
  var myButton = document.getElementById("myButton");
  
  myButton.addEventListener("click", function() {
      // Code to be executed when the button is clicked
      console.log("Button clicked!");
      // Add your custom logic here
  });
  
  // Example: Make an AJAX request
  var myData = {
      name: "John",
      age: 30
  };
  
  // Using Fetch API
  fetch("/api/data", {
      method: "POST",
      body: JSON.stringify(myData),
      headers: {
          "Content-Type": "application/json"
      }
  })
  .then(function(response) {
      return response.json();
  })
  .then(function(data) {
      // Handle the response data
      console.log(data);
      // Add your custom logic here
  })
  .catch(function(error) {
      // Handle any errors
      console.error(error);
  });
  
  // Example: Toggle a CSS class on an element
  var myElement = document.getElementById("myElement");
  
  myElement.addEventListener("click", function() {
      // Toggle the CSS class
      myElement.classList.toggle("highlight");
  });
});
