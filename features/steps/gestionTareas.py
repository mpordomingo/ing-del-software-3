from behave import *

from chronos.models import *


@given('soy empleado')
def step_impl(context):
    pass


@given('a user wants to add a task with the following values')
def step_impl(context):
    pass


@when('the user adds the task')
def step_impl(context):
    task = Task(title=context.table[0]['title'],
                description=context.table[0]['description'],
                state=context.table[0]['state'])
    context.task = task
    task.save()


@then('the task is saved and linked to a project or initiative')
def step_impl(context):
    taskSet = Task.tasks.filter(code=context.task.code)
    assert taskSet.first() is not None
    taskSet.delete()



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


@when('modifico los atirbutos descripcion, estado y tiempos de la tarea')
def step_impl(context):
    pass


@then ('se registran los cambios')
def step_impl(context):
    pass
