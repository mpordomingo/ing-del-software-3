from behave import *
from chronos.models import *
from chronos.controllers.taskController import TaskController
import time
@given('that I am about to start a task')
def step_impl(context):
    context.searchResult = TaskController.filter_by_code(code=1)

@when('I select the task and start the stopwatch for 5 seconds')
def step_impl(context):
    stopwatch = Stopwatch(breakTime=time.time()+5, recordedTime=0)
    stopwatch.start()
    pass
@then('time begins to be measured until the break')
def step_impl(context):
    pass
