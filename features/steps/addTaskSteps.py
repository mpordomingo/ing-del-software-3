from behave import *

from chronos.models import *




@given('a user wants to add a task')
def step_impl(context):
    pass


@when('the user adds the task with the following values')
def step_impl(context):
    task = Task(title=context.table[0]['title'],
                description=context.table[0]['description'],
                state=context.table[0]['state'])
    context.task = task
    task.save()


@then('the task is saved')
def step_impl(context):
    taskSet = Task.tasks.filter(code=context.task.code)
    assert taskSet.first() is not None
    taskSet.delete()


