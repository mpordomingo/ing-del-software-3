from behave import *

from chronos.controllers.taskController import TaskController
from chronos.models import *


@given("a set of tasks")
def step_impl(context):
    tasks = []
    for row in context.table:
        task = Task(title=row['title'], description=row['description'], state=row['state'])
        task.save()
        tasks.append(task)
    context.tasks = tasks


@given("no tasks are stored")
def step_impl(context):
    Task.tasks.all().delete()


@when("the user filters tasks by code")
def step_impl(context):
    code = context.tasks[0].code
    context.searchResult = TaskController.filter_by_code(code=code)


@then("the task with that code is shown")
def step_impl(context):
    assert context.searchResult is not None \
           and context.searchResult.code == context.tasks[0].code
    context.searchResult.delete()


@when("the user filters tasks by description")
def step_impl(context):
    context.searchResult = TaskController.filter_by_description(description=context.table[0]['description'])


@then("tasks with that description are shown")
def step_impl(context):
    assert context.searchResult is not None and len(context.searchResult) == int(context.table[0]['results quantity'])
    context.searchResult.delete()


@when('the user filters by tasks in "{state}" state')
def step_impl(context, state):
    context.searchResult = TaskController.filter_by_state(state=state)


@then('{quantity} tasks with that state are shown')
def step_impl(context, quantity):
    print(list(context.searchResult))
    assert context.searchResult is not None and len(context.searchResult) == int(quantity)
    context.searchResult.delete()


@when('the user filters tasks by code "{code}" and none are found')
def step_impl(context, code):
    context.searchResult = TaskController.filter_by_code(code=code)


@then('the following warning is shown')
def step_impl(context):
    print(list(context.searchResult))
    assert context.searchResult is not None and context.searchResult == context.table[0]['warning']


@when('the user filters tasks by description "{description}" and none are found')
def step_impl(context, description):
    context.searchResult = TaskController.filter_by_description(description=description)


@when('the user filters tasks by state "{state}" and none are found')
def step_impl(context, state):
    context.searchResult = TaskController.filter_by_state(state=state)