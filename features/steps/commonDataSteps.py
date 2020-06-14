from behave import *

from chronos.models import *

@given('soy empleado')
def step_impl(context):
    pass

@given("I am an employee")
def step_imp(context):
    pass

@given("the following values for a task")
def step_impl(context):
    context.samples = context.table

@given("the following default values for a task")
def step_impl(context):
    context.defaultTask = context.table[0]

