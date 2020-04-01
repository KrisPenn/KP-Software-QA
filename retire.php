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
  </style>
  <meta charset="UTF-8">
  <title>Retire Savings Calc Page</title>
</head>
<body>
  <h1>Welcome to the Retirement Savings Calculator</h1>
  <?php
  // INITAL VALUES
    $age = 21;
    $salary = 60000;
    $savings = 20;
    $goal = 100000;
    $total = 0;
    $met = False;

    if (isset($_POST['submit']))
    {
      $age = $_POST['age'];
      $age2 = $_POST['age'];
      $salary = $_POST['salary'];
      $savings = $_POST['savings'];
      $goal = $_POST['goal'];

      $yearly = (($savings / 100) * $salary) * 1.35;

      $tick = True;
      while ($tick == True) {
        $total += $yearly;
        $age2 += 1;
        if ($total >= $goal)
        {
          $met = True;
          $_SESSION['age'] = $age;
          $tick = False;
        }
        elseif($age2 >= 100)
        {
          $tick = False;
        }
      }
    }
    if (is_numeric($age) && $age >= 0 && $age != "")
    {
      $ageErr = "";
    }
    else
    {
      $ageErr = "(Age must be an integer greater than 0.)";
    }


    if (is_numeric($salary) && $salary >= 0 && $salary != "")
    {
      $salaryErr = "";
    }
    else
    {
      $salaryErr = "(Salary must be an integer greater than 0.)";
    }


    if (is_numeric($savings) && $savings >= 0 && $savings != "")
    {
      $savingsErr = "";
    }
    else
    {
      $savingsErr = "(Savings must be an integer greater than 0.)";
    }

    if (is_numeric($goal) && $goal >= 0 && $goal != "")
    {
      $goalErr = "";
    }
    else
    {
      $goalErr = "(Goal must be an integer greater than 0.)";
    }
  ?>

    <form method="post" action="retire.php">

        Age: <input type="text" size="5" name="age" value="<?php echo $age ?>">
        <span class="error"><?php echo $ageErr ?></span>
        <br><br>

        Yearly Salary: <input type="text" size="15" name="salary" value="<?php echo $salary ?>">
        <span class="error"><?php echo $salaryErr ?></span>
        <br><br>

        Percentage saved from Salary: <input type="text" size="4" name="savings" value="<?php echo $savings ?>">
        <span class="error"><?php echo $savingsErr?></span>
        <br><br>

        Goal: <input type="text" size="3" name="goal" value="<?php echo $goal ?>">
        <span class="error"><?php echo $goalErr ?></span>
        <br><br>

        <input type="submit" name="submit" value="Calculate">
    </form>
    <br><br>

    <?php
    if ($met == True)
    {
      echo "<p>You will reach your goal when you are ", $age2, " years old.</p>";
    }
    else
    {
      echo "<p>You will not reach your goal before you are 100 years old.</p>";
    }
    ?>

    <p><a href="start_page.php">Home</a></p>
</body>
</html>
