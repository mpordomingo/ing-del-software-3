Feature: Modify task attributes
  As an employee, I want to modify a task so that I can complete it correctly.


  Scenario: Modify task description
    Given I am an employee
    When I modify the attributes description, status and times of the task
    Then changes are recorded
  Scenario: Assign invalid attributes
    Given I am an employee
    When I assign invalid attributes -invalid states or times-
    Then I get a notification of the situation

