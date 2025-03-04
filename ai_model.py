<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AK Study Planner - AI Study Helper</title>
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>

  <div class="container">
    <!-- Logo (Optional) -->
    <img src="logo.png" alt="AK Study Planner Logo" class="logo">

    <h1>AK Study Planner - AI Study Helper</h1>
    <p>Your AI-powered study planner to help you stay on track and study smarter!</p>

    <!-- Study Plan Form -->
    <div class="form-container">
      <label for="subject"><i class="fas fa-book"></i> Subject:</label>
      <input type="text" id="subject" placeholder="Enter subject name">

      <label for="study-time"><i class="fas fa-clock"></i> Study Time (in hours):</label>
      <input type="number" id="study-time" placeholder="Enter hours">

      <label for="difficulty"><i class="fas fa-tasks"></i> Difficulty Level:</label>
      <select id="difficulty">
        <option value="Easy">Easy</option>
        <option value="Medium">Medium</option>
        <option value="Hard">Hard</option>
      </select>

      <button id="generate-btn"><i class="fas fa-magic"></i> Generate Study Plan</button>
    </div>

    <!-- Output Area -->
    <div id="output-container">
      <h2>📖 Your AI-Generated Study Plan:</h2>
      <p id="output-text">Your study plan will appear here...</p>
    </div>
  </div>

  <script src="script.js"></script>
</body>
</html>

