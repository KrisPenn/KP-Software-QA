<?php
  session_start()
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <style>
      .error {
        color: #FF0000;
      }
      table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
      }

      td, th {
        border: 1px solid black;
        text-align: left;
        padding: 8px;
      }
      tr:nth-child(even) {
        background-color: #dddddd;
      }
  </style>
  <meta charset="UTF-8">
  <title>User Page</title>
</head>
<body>
  <h1>Welcome to the Body Mass Index Calculator</h1>
  <?php
  // INITAL VALUES
    $weight = 0;
    $heightFeet = 0;
    $heightInches = 0;
    $calculated = False;

    if (isset($_POST['submit']))
    {
      $weight = $_POST['weight'];
      $heightFeet = $_POST['heightFeet'];
      $heightInches = $_POST['heightInches'];
    }


    if (is_numeric($weight) && $weight >= 0 && $weight != "")
    {
      $weightErr = "";
    }
    else
    {
      $weightErr = "(weight must be an integer greater than 0.)";
    }


    if (is_numeric($heightFeet) && $heightFeet >= 0 && $heightFeet != "")
    {
      $heightFeetErr = "";
    }
    else
    {
      $heightFeetErr = "(Feet must be an integer greater than 0.)";
    }


    if (is_numeric($heightInches) && $heightInches >= 0 && $heightInches < 12 && $heightInches != "")
    {
      $heightInchesErr = "";
    }
    else
    {
      $heightInchesErr = "(Inches must be an integer greater than 0 and less than 12.)";
    }

    if ($heightFeet != 0)
    {
      $totalHeight = (($heightFeet * 12) + $heightInches) * 0.025;
      $totalHeight *= $totalHeight;
      $realWeight = $weight * .45;
      $BMI = $realWeight / $totalHeight;
      $calculated = True;
    }
  ?>

    <form method="post" action="bmi.php">

        <b>Weight:</b> <input type="text" size="5" name="weight" value="<?php echo $weight ?>">
        <span class="error"><?php echo $weightErr ?></span>
        <br><br>

        <b>Height:</b><br> Feet: <input type="text" size="2" name="heightFeet" value="<?php echo $heightFeet ?>">
        <span class="error"><?php echo $heightFeetErr ?></span>
        <br>

        Inches: <input type="text" size="2" name="heightInches" value="<?php echo $heightInches ?>">
        <span class="error"><?php echo $heightInchesErr?></span>
        <br><br>

        <input type="submit" name="submit" value="Calculate">
    </form>
    <br><br>

    <?php
    if ($calculated == True)
    {
      echo "<p>You have a BMI of ", $BMI, ".</p>";
    }
    ?>

    <table style="width:30%">
      <tr>
        <th>Category</th>
        <th>BMI</th>
      </tr>
      <tr>
        <td>Underweight</td>
        <td>0 - 18.5</td>
      </tr>
      <tr>
        <td>Normal Weight</td>
        <td>18.5 - 25</td>
      </tr>
      <tr>
        <td>Overweight</td>
        <td>25 - 30</td>
      </tr>
      <tr>
        <td>Obese</td>
        <td>30+</td>
      </tr>
    </table>

    <br><br>
    <p><a href="start_page.php">Home</a></p>
</body>
</html>
