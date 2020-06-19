Feature: Activate Stopwatch
  As an employee, I want to activate the stopwatch so that I can meassure the time of my tasks automatically

  Scenario: Activate stopwatch
    Given that I am about to start a task
    When I select the task and start the stopwatch for 5 seconds
    Then time begins to be measured until the break