from behave import *

from chronos.models import Task


@given('soy empleado')
def step_impl(context):
    pass


@when('cuando doy una tarea de alta')
def step_impl(context):
    task = Task(title="Implementar PSA Cloud Spring ERP para cliente ",
                description="Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades.",
                state="To Do",
                assigneeId=2,
                projectId=1)
    task.save()


@then('se registra la tarea y se vincula a un proyecto-inciativa-tema')
def step_impl(context):
    taskSet = Task.tasks.filter(title="Implementar PSA Cloud Spring ERP para cliente ", projectId=1).first()
    assert (taskSet is not None) and (taskSet.projectId == 1)



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
