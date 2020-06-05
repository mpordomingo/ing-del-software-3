Feature: add a task
  As an employee, I want to add a task so that I can better organize my work.

  Scenario: Add a task
    Given I am an employee
    When I add a task
    Then the task is saved and linked to a project or initiative