from behave import *
from chronos.models import *
import time


@given('that I am measuring the time with the stopwatch for 2 seconds')
def step_impl(context):
    stopwatch = Stopwatch()
    stopwatch.start()
    time.sleep(2)
    context.stopwatch = stopwatch
    assert int(stopwatch.initialTime) + 2 == int(time.time())


@when('I pause it for 2 seconds')
def step_impl(context):
    context.stopwatch.pause()
    time.sleep(2)
    assert int(context.stopwatch.initialInactivity) + 2 == int(time.time())


@then('when I return I can resume it and use it for 1 second, recording 3s')
def step_impl(context):
    context.stopwatch.resume()
    time.sleep(1)
    context.stopwatch.stop()
    assert int(context.stopwatch.recordedTime) == 3
