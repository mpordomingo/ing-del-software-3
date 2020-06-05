Feature: dar tarea de alta
  Como empleado, quiero dar una tarea de alta cuando gestiono mis tareas para poder organizar mi trabajo.

  Scenario: Dar tarea de alta
    Given soy empleado
    When cuando doy una tarea de alta
    Then se registra la tarea y se vincula a un proyecto-inciativa-tema