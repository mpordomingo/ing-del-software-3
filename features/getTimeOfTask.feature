Feature: get the time of a task
  As an employee, I want to get the time of a task

  Scenario: A task is in progress
    Given a user wants to get the time of a task
    When the user pause the task
    Then the task return the time lapse


  Scenario: A task is in progress
    Given one work cycle finished and a rest cycle finished
    When the user wants to see the cycles count
    Then task has cycles