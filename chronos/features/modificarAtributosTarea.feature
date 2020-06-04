Feature: Modificar atributos de una tarea
  Como empleado, quiero modificar una tarea para poder realizarla correctamente.

  Scenario: Modificar descripcion de una tarea
    Given soy empleado
    When modifico los atributos descripcion, estado y tiempos de la tarea
    Then se registran los cambios