Feature: Filter tasks
  As an employee I want to filter tasks when I view them so that I can work with the ones that I need.

  Background:
    Given a set of tasks
    | title                                       | description                                                    | state       |
    | Resolver vulnerabilidades PSA ERP           | Resolver vulnerabilidades de PSA Spring ERP                    | To Do       |
    | Implementar PSA Spring ERP                  | Coordinar con client la implementacion de PSA Spring ERP       | To Do       |
    | Probar implementacion de PSA Spring ERP     | Coordinar con cliente la prueba de la implementacion de PSA ERP| Done        |
    | Integraciones de PSA Spring ERP             | Integrar el PSA Spring ERP                                     | In Progress |

  Scenario: user filters by task code
    Given a user
    When the user filters tasks by code
    Then the task with that code is shown

  Scenario: user filters by task description
    Given a user
    When the user filters tasks by description
    |description     |
    |PSA Spring ERP  |
    Then tasks with that description are shown
    |results quantity     |
    |3                    |

  Scenario Outline: user filters by tasks state
    Given a user
    When the user filters by tasks in "<state>" state
    Then <quantity> tasks with that state are shown
    Examples:
      |state       | quantity            |
      |To Do       | 2                   |
      |In Progress | 1                   |
      |Done        | 1                   |


  Scenario: user filters by code and no tasks are found
   Given a user
    When the user filters tasks by code "12345" and none are found
    Then the following warning is shown
    |warning                                 |
    |No se econtro una tarea para ese codigo.|

  Scenario: user filters by description and no tasks are found
    Given a user
    When the user filters tasks by description "No description like this" and none are found
    Then the following warning is shown
    |warning                                      |
    |No se encontraron tareas con esa descripcion.|

  Scenario Outline: user filters by state and no tasks are found
    Given a user
    Given no tasks are stored
    When the user filters tasks by state "<state>" and none are found
    Then the following warning is shown
    |warning                                      |
    |No se encontraron tareas en ese estado.|
    Examples:
      |state       |
      |To Do       |
      |In Progress |
      |Done        |