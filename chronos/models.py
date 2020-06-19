from django.db import models
from functools import reduce

import time


class Task(models.Model):
    __VALID_STATES__ = [
        (1, "To Do"),
        (2, "In Progress"),
        (3, "Done")
    ]

    code = models.AutoField(null=False, primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.CharField(default="", null=False, max_length=255)
    state = models.CharField(default="To Do", max_length=15, choices=__VALID_STATES__)

    tasks = models.Manager()

    @staticmethod
    def valid_states():
        return list(map((lambda x: x[1]), Task.__VALID_STATES__))

    def save(self, *arg, **args):
        assert self.title, "Se debe especificar un titulo para la tarea."
        assert self.state in self.valid_states(), "El estado especificado no es valido"
        super().save(*args, **args)


class Stopwatch(models.Model):
    breakTime = models.IntegerField()
    recordedTime = models.IntegerField()

    def start(self):
        now = time.time()
        meassure_time = 0
        while time.time() < self.breakTime:
            pass
        self.recordedTime = self.breakTime
