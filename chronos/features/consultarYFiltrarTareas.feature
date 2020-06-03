Feature:
  Scenario: filtrar por codigo de tarea
    Given soy empleado
    When filtro las tareas por codigo
    Then se muestra la tarea correspondiente al codigo indicado

  Scenario: filtrar por descripcion de tarea
    Given soy empleado
    When filtro por descripcion de tarea
    Then se me muestran las tareas que contienen la descripcion indicada



#Dado que soy un trabajador, cuando filtro por código para consultar una tarea, entonces se muestra la tarea correspondiente al código indicado.

#Dado que soy un trabajador, cuando filtro por descripción para consultar las tareas, entonces se muestran las tareas que contienen la descripción indicada.

#Dado que soy un trabajador, cuando filtro por estado en la consulta de tareas, entonces se muestran las tareas que se encuentran en  el estado indicado.

#Dado que soy trabajador, cuando consulto tareas que no me estan asignadas, entonces se me muestra una advertencia indicando esta situación.