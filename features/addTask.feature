Feature: add a task
  As an employee, I want to add a task so that I can better organize my work.

  Background:
    Given the following values for a task
    | title                                         | description                                                                                   | state |
    | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades. | To Do |

    Given the following default values for a task
    | state |
    |To Do  |

  Scenario: Add a task with all fields
    Given a user wants to add a task
    When the user adds the task with all the values
    Then the task is saved


  Scenario: Add a task with the title only
    Given a user wants to add a task without description or state
    When the user adds the task with the title value only
    Then the task is saved with the title, an empty description and the default state


  Scenario: Add a task with the title and description values
    Given a user wants to add a task without specifying state
    When the user adds the task with the title and description values
    Then the task is saved with the title, a description and the default state


  Scenario: Add a task without title
    Given a user wants to add a task without specifying a title
    Given the following required state warning
    | warning |
    | Se debe especificar un titulo para la tarea. |
    When the user adds the task without the title
    Then a warning is shown indicating the task cannot be created


  Scenario: Add a task with invalid state
    Given a user wants to add a task with an invalid state
    Given the following warning and invalid state
    | warning                             | invalid state    |
    | El estado especificado no es valido | an invalid state |
    When the user adds the task with the invalid state
    Then an invalid state warning is shown