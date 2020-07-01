Feature: Pause Stopwatch
As an employee, I want to pause the stopwatch so that I can stop working for any circumstance
  Scenario: Pause Stopwatch
    Given that I am measuring the time with the stopwatch for 2 seconds
    When I pause it for 2 seconds
    Then when I return I can resume it and use it for 1 second, recording 3s