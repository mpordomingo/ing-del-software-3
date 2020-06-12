from behave import *

from chronos.models import *


@given("I am an employee with a task that consists of the following values")
def step_imp(context):
    task = Task(title=context.table[0]['title'],
                description=context.table[0]['description'],
                state=context.table[0]['state'])
    context.task = task
    task.save()


@when('I modify the description and status of the task')
def step_impl(context):
    task = context.task
    task.description = context.table[0]['description']
    task.state = context.table[0]['state']
    context.testData = context.table[0]
    task.save()


@then('changes are recorded')
def step_impl(context):
    taskSet = Task.tasks.filter(code=context.task.code)
    task = taskSet.first()
    testData = context.testData
    assert task is not None and task.state == testData['state'] and task.description == testData['description']
    taskSet.delete()


@when('I assign invalid attributes -invalid states or times-')
def step_impl(context):
    pass


@then ('I get a notification of the situation')
def step_impl(context):
    pass