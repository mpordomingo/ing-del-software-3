from behave import *

from chronos.models import *


@given('a user wants to add a task')
def step_impl(context):
    pass


@when('the user adds the task with all the values')
def step_impl(context):
    task = Task(title=context.samples[0]['title'],
                description=context.samples[0]['description'],
                state=context.samples[0]['state'])
    context.task = task
    task.save()


@then('the task is saved')
def step_impl(context):
    taskSet = Task.tasks.filter(code=context.task.code)
    assert taskSet.first() is not None
    taskSet.delete()


@given("a user wants to add a task without description or state")
def step_impl(context):
    pass


@when('the user adds the task with the title value only')
def step_impl(context):
    task = Task(title=context.samples[0]['title'])
    context.task = task
    task.save()


@then('the task is saved with the title, an empty description and the default state')
def step_impl(context):
    tasks = Task.tasks.filter(code=context.task.code)
    task = tasks.first()
    assert task is not None \
           and task.title == context.task.title \
           and task.state == context.defaultTask['state'] \
           and task.description == ""

    task.delete()


@given('a user wants to add a task without specifying state')
def step_impl(context):
    pass


@when('the user adds the task with the title and description values')
def step_impl(context):
    task = Task(title=context.samples[0]['title'], description=context.samples[0]['description'])
    context.task = task
    task.save()


@then('the task is saved with the title, a description and the default state')
def step_impl(context):
    tasks = Task.tasks.filter(code=context.task.code)
    task = tasks.first()
    assert task is not None \
           and task.description == context.samples[0]['description'] \
           and task.state == context.defaultTask['state']

    tasks.delete()


@given('a user wants to add a task without specifying a title')
def step_impl(context):
    pass


@given('the following required state warning')
def step_impl(context):
    context.expectedWarning = context.table[0]['warning']


@when('the user adds the task without the title')
def step_impl(context):
    context.exception = ""
    try:
        task = Task()
        context.task = task
        task.save()
    except Exception as e:
        context.exception = str(e)


@then('a warning is shown indicating the task cannot be created')
def step_impl(context):
    assert context.exception == context.expectedWarning


@given('a user wants to add a task with an invalid state')
def step_impl(context):
    pass


@given('the following warning and invalid state')
def step_impl(context):
    context.expectedWarning = context.table[0]['warning']
    context.invalidState = context.table[0]['invalid state']


@when('the user adds the task with the invalid state')
def step_impl(context):
    context.exception = ""
    try:
        task = Task(title=context.samples[0]['title'], state=context.invalidState)
        context.task = task
        task.save()
    except Exception as e:
        context.exception = str(e)


@then('an invalid state warning is shown')
def step_impl(context):
    assert context.exception == context.expectedWarning

