from django.db import models


class StateField(models.Field):

    name = ""

    def __init__(self, state, *args, **kwargs):
        kwargs['max_length'] = 104
        name = state
        super().__init__(*args, **kwargs)


class Task(models.Model):
    code = models.IntegerField(null=False, primary_key=True)
    description = models.CharField()
    state = models.StateField()
