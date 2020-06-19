Feature: Modify task attributes
  As an employee, I want to modify a task so that I can complete it correctly.


  Scenario: Modify task description
    Given I am an employee with a task that consists of the following values
    | title                                         | description                                                                                   | state |
    | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades. | To Do |

    When I modify the description and status of the task
    | description                                                                                   | state |
    | Coordinar con el cliente la prueba del sistema PSA Cloud Spring ERP.                          | In Progress |

    Then changes are recorded

  Scenario: Assign invalid attributes
    Given I am an employee with a task that consists of the following values
     | title                                         | description                                                                                   | state |
    | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades. | To Do |
    When I assign the following invalid state
    | state |
    | Not Done |
    Then I get a notification of the wrong state

