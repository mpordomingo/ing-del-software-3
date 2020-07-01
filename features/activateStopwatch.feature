Feature: Activate Stopwatch
  As an employee, I want to activate the stopwatch so that I can meassure the time of my tasks automatically

  Scenario: Activate stopwatch
    Given that I am about to work on a task
    When I use the stopwatch for 5 seconds
    Then it is save in the TimeRecord
