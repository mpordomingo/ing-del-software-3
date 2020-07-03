from behave import *
from chronos.models import *
from chronos.controllers.taskController import TaskController
import time
import datetime


@given('a user wants to get the time of a task')
def step_impl(context):
    stopwatch = Stopwatch()

    task = Task(title='Create installer',
                description='Installer for PSA application',
                state='To Do')
    stopwatch.start()
    context.stopwatch = stopwatch
    context.task = task
    task.save()


@when('the user pause the task')
def step_impl(context):
    context.stopwatch.stop()


@then('the task return the time lapse')
def step_impl(context):
    assert context.stopwatch.recordedTime is not 0


@given('one work cycle finished and a rest cycle started')
def step_impl(context):
    task = Task(title='Create installer',
                description='Installer for PSA application',
                state='To Do')

    first_time_record = TimeRecord(cycle=WorkCycle())
    second_time_record = TimeRecord(cycle=RestCycle())

    task.record(first_time_record)
    task.record(second_time_record)
    context.task = task


@when('the user wants to see the cycles count')
def step_impl(context):
    pass


@then('task has cycles')
def step_impl(context):
    assert context.task.getCycles.count is 2

