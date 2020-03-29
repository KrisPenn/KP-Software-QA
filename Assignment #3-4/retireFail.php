<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Log in to Website</title>
  <style>
    input {
      margin-bottom: 0.5em;
    }
    .error {
      color: #FF0000;
    }
  </style>
</head>
<body>
  <h1>Fail!</h1>
  <p>You will not meet your goal by the time you are 100 years old.</p>
  <?php
  session_start();
  session_unset();
  session_destroy();
  ?>
  <br><br>
  <p><a href="start_page.php">Home</a></p>
</body>
