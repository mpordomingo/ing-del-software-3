Feature: Visualize tasks
  As an employee, I want to visualize my tasks so that I can see what tasks I worked on

  Scenario: visualize tasks
    Given a user

    When he wants to visualize his tasks:
    | title  | description                 | state |
    | Task 1 | Some description for task 1 | To Do |
    | Task 2 | Some description for task 2 | To Do |
    | Task 3 | Some description for task 3 | To Do |
    | Task 4 | Some description for task 4 | To Do |

    Then all his tasks are shown