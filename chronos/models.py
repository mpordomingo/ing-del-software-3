from django.db import models
from functools import reduce

from threading import Thread
from time import sleep
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


def timer(time_record, times):
    sleep(time)
    handler(event='FINISH_TIME_RECORD')


class Stopwatch(models.Model):
    recordedTime: float = models.FloatField()
    initialTime: float = 0
    initialInactivity: float = 0
    inactivityTime: float = 0

    def start(self, times):
        time_thread = Thread(target=timer(times))
        self.initialTime = time.time()

    def stop(self):
        now: float = time.time()
        self.recordedTime = now - self.initialTime - self.inactivityTime

    def pause(self):
        self.initialInactivity = time.time()

    def resume(self):
        now: float = time.time()
        self.inactivityTime += now - self.initialInactivity


class Cycle(models.Model):
    time = models.FloatField()


class WorkCycle(Cycle):
    time = models.FloatField(default=25)


class RestCycle(Cycle):
    time = models.FloatField(default=5)

class Handler(models.Model):
    timer = models.OneToOneField(
        Timer,
        on_delete=models.CASCADE,
        primary_key=True,
    )
class TimeRecord(models.Model):
    startTime = models.TimeField()
    endTime = models.TimeField()
    date = models.DateField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    cycle = models.OneToOneField(
        Cycle,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    stopwatch = models.OneToOneField(
        Stopwatch,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    handler = models.OneToOneField(
        Handler,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    timer_thread = Thread(target=timer(handler, cycle.time))

    def start(self):
        self.timer_thread.start()

    def pause(self):
        self.timer_thread.

    def stop(self):
        self.stopwatch.stop()



