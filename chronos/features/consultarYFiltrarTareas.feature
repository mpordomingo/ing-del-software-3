Feature: Consulta y filtrado de tareas
  Como trabajador, quiero consultar las tareas y filtrarlas por atributos
  codigo, descripcion, estado, asignacion y tiempos para poder organizar mi trabajo.

  Scenario: filtrar por codigo de tarea
    Given soy empleado
    When filtro las tareas por codigo
    Then se muestra la tarea correspondiente al codigo indicado

  Scenario: filtrar por descripcion de tarea
    Given soy empleado
    When filtro por descripcion de tarea
    Then se muestran las tareas que contienen la descripcion indicada

  Scenario: filtrar por estado de la tarea
    Given soy empleado
    When filtro por estado de la tarea
    Then se muestran las tareas que estan en el estado indicado

  Scenario:
    Given soy empleado
    When consulto tareas y no se encuentra ninguna
    Then se muestra una advertencia indicando esta situacion

