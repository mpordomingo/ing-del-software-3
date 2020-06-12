Feature: add a task
  As an employee, I want to add a task so that I can better organize my work.

  Scenario: Add a task
    Given a user wants to add a task
    When the user adds the task with the following values
     | title                                         | description                                                                                   | state |
     | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades. | To Do |

    Then the task is saved
