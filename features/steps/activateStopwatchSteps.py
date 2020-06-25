from behave import *
from chronos.models import *
from chronos.controllers.taskController import TaskController
import time
import datetime


@given('that I am about to work on a task')
def step_impl(context):
    context.searchResult = TaskController.filter_by_code(code=1)


@when('I use the stopwatch for 5 seconds')
def step_impl(context):
    stopwatch = Stopwatch()
    stopwatch.start()
    time.sleep(5)
    stopwatch.stop()
    context.stopwatch = stopwatch
    assert int(stopwatch.recordedTime) == 5


@then('it is save in the TimeRecord')
def step_impl(context):
    init = time.localtime(context.stopwatch.initialTime)
    finish = time.localtime(context.stopwatch.initialTime + context.stopwatch.recordedTime)
    record = TimeRecord(startTime=datetime.time(init.tm_hour, init.tm_min, init.tm_sec),
                        endTime=datetime.time(finish.tm_hour, finish.tm_min, finish.tm_sec),
                        date=datetime.date(init.tm_year, init.tm_mon, init.tm_mday))
    record.save()
    assert record.startTime == datetime.time(init.tm_hour, init.tm_min, init.tm_sec) and \
           record.endTime == datetime.time(finish.tm_hour, finish.tm_min, finish.tm_sec) and \
           record.date == datetime.date(init.tm_year, init.tm_mon, init.tm_mday)
