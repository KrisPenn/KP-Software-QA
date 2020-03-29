<?php
  session_start();
  $age = $_SESSION['age'];
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Savings Success</title>
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
  <h1>Success!</h1>
  <p>You will meet your goal by the time you are <?php echo $age; ?> years old.</p>
  <?php
  session_unset();
  session_destroy();
  ?>
  <br><br>
  <p><a href="start_page.php">Home</a></p>
</body>
