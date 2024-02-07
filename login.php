<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dry Skin</title>
    <link rel="stylesheet" type="text/css" href="style_index.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

<style>
  .log {
    font-family: Arial, sans-serif;
    
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

.signup-container {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-top: -90px;
    width: 500px;
}


label {
    margin-bottom: 8px;
}

input {
    padding: 8px;
    margin-bottom: 16px;
}

button {
    background-color: #4caf50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

#error-message {
    color: #ff0000;
    margin-top: 10px;
}

</style>
</head>

<body>
  <div class="mani">
    <div class="showcase">
      <img src="bg.jpg">
    </div>
  
    
    <header style="height: 19.5em;">
      <div class="d1">
        <div class="gradient-border" style="height: 166px; width: 520px;">
          <img src="lol.png" style="height:166px; z-index:4; width:520px; ">
        </div>
        
        <div class="cn" style="float:right; margin-top:-80px; margin-right:100px">
          <form class="d-flex" role="search">
            <button formaction="about us.html" class="btn btn-outline-success" type="submit" style=" color:antiquewhite;background: linear-gradient(90deg, #72a016, rgb(182, 128, 47));width:270px;height:70px ">About  US</button>
        
        <button formaction="contactus.html" class="btn btn-outline-success" type="submit" style=" color:antiquewhite;background: linear-gradient(90deg, #72a016, rgb(182, 128, 47));width:270px;height:70px;margin-left:30px; ">CONTACT US</button>
        </form>
        </div>
    <!--<h1 style="padding: 15px;">Welcome to Derma Home</h1>-->
      </div>
<div id="navbar">
    <nav class="menu">
      <ol>
          <li class="menu-item"><a href="index.html">Home</a></li>
          
          <li class="menu-item">
            <a href="#0">Skin Type</a>
            <ol class="sub-menu">
              <li class="menu-item"><a href="normal skin.html">Normal Skin </a></li>
              <li class="menu-item"><a href="dry skin.html">Dry Skin</a></li>
              <li class="menu-item"><a href="oily skin.html">Oily Skin</a></li>
             
              <li class="menu-item"><a href="combination skin.html">Combination Skin</a></li>
            </ol>
          </li>
          <li class="menu-item"><a href="skincare at home.html">Skin Care At Home</a></li>
          <li class="menu-item"><a href="hair_care.html">Hair Care At Home</a></li>
          <li class="menu-item">
            <a href="#0">Products</a>
            <ol class="sub-menu">
              <li class="menu-item"><a href="men.html">Men</a></li>
              <li class="menu-item"><a href="women.html">Women</a></li>
            </ol>
          </li>
          
          
        </ol>
    </nav>
    <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" >
            <button class="btn btn-outline-success" type="submit" style="background: linear-gradient(90deg, #16a085, rgb(182, 155, 47)); ">Search</button>
          </form>
        </div>
    
    </header>
    <div class="log">
      <div class="signup-container">
          <h2>Sign Up</h2>
          <div class="form">
          <form id="signupForm" action="signup.php" method="post" style=" display: flex; flex-direction: column;">
              <label for="username">Username:</label>
              <input type="text" id="username" name="username" required>
  
              <label for="email">Email:</label>
              <input type="email" id="email" name="email" required>
  
              <label for="password">Password:</label>
              <input type="password" id="password" name="password" required>
  
              <button type="button" onclick="validateForm()">Sign Up</button>
          </form>
        </div>
  
          <div id="error-message"></div>
      </div>
  
    </div>
    
    <script>
      window.onscroll = function() {myFunction()};
      
      var navbar = document.getElementById("navbar");
      var sticky = navbar.offsetTop;
      
      function myFunction() {
        if (window.pageYOffset >= sticky) {
          navbar.classList.add("sticky")
        } else {
          navbar.classList.remove("sticky");
        }
      }
      function validateForm() {
        var username = document.getElementById("username").value;
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;
    
        // Simple validation, you can enhance it based on your requirements
        if (username === "" || email === "" || password === "") {
            document.getElementById("error-message").innerText = "All fields are required";
        } else {
            document.getElementById("signupForm").submit();
        }
    }
    
      </script>
</body>
</html>