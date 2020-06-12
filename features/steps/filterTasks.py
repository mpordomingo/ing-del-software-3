from behave import *

from chronos.models import *


@when('filtro las tareas por codigo')
def step_impl(context):
    pass


@then('se muestra la tarea correspondiente al codigo indicado')
def step_impl(context):
    pass


@when('filtro por descripcion de tarea')
def step_impl(context):
    pass


@then('se muestran las tareas que contienen la descripcion indicada')
def step_impl(context):
    pass


@when('filtro por estado de la tarea')
def step_impl(context):
    pass


@then('se muestran las tareas que estan en el estado indicado')
def step_impl(context):
    pass


@when('consulto tareas y no se encuentra ninguna')
def step_impl(context):
    pass


@then('se muestra una advertencia indicando esta situacion')
def step_impl(context):
    pass


