from behave import *
from chronos.models import *

@given("a user")
def step_imp(context):
    pass

@when('he wants to visualize his tasks')
def step_impl(context):
    task1 = Task(title=context.table[0]['title'], description=context.table[0]['description'], state=context.table[0]['state'])
    task2 = Task(title=context.table[1]['title'], description=context.table[1]['description'], state=context.table[1]['state'])
    task3 = Task(title=context.table[2]['title'], description=context.table[2]['description'], state=context.table[2]['state'])
    task4 = Task(title=context.table[3]['title'], description=context.table[3]['description'], state=context.table[3]['state'])
    
    task1.save()
    task2.save()
    task3.save()
    task4.save()

    context.tasks = Task.tasks.all()
    assert (len(context.tasks) is 4)

@then('all his tasks are shown')
def step_impl(context):
    pass