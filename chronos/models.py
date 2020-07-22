from django.db import models
import datetime
import math

class Task(models.Model):
    __VALID_STATES__ = [
        (1, "To Do"),
        (2, "In Progress"),
        (3, "Done")
    ]

    code = models.AutoField(null=False, primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.CharField(default="", null=True, max_length=255)
    state = models.CharField(default="To Do", max_length=15, choices=__VALID_STATES__)

    tasks = models.Manager()

    @staticmethod
    def valid_states():
        return list(map((lambda x: x[1]), Task.__VALID_STATES__))

    def save(self, *arg, **args):
        super().save(*args, **args)

    def finalize(self):
        assert self.state == "In Progress", "La tarea debe estar en estado 'In Progress'"
        self.state = "Done"

    def start(self):
        assert self.state == "To Do", "La tarea debe estar en estado 'To Do'"
        self.state = "In Progress"


class Cycle(models.Model):
    totalTime = models.FloatField(null=True)


class WorkCycle(Cycle):
    time = models.FloatField(default=1500)


class RestCycle(Cycle):
    time = models.FloatField(default=300)


class TimeRecord(models.Model):
    code = models.AutoField(null=False, primary_key=True)
    startTime = models.TimeField()
    endTime = models.TimeField(null=True)
    date = models.DateField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    restCycle = models.OneToOneField(
        RestCycle,
        on_delete=models.CASCADE
    )
    workCycle = models.OneToOneField(
        WorkCycle,
        on_delete=models.CASCADE
    )

    records = models.Manager()

    def save(self, *arg, **args):
        assert self.task.state != "Done", "La tarea se ha finalizado. "
        super().save(*args, **args)

    def start(self):
        self.startTime = datetime.datetime.now().time()

    def stop(self):
        assert self.endTime is None, "Este registro de tiempo ya fue finalizado."
        self.endTime = datetime.datetime.now().time()

    def ustop(self):
        if self.endTime is None:
            self.endTime = datetime.datetime.now().time()

    def time_elapsed(self):
        if self.startTime is None:
            return 0
        if self.endTime is None:
            end_time = datetime.datetime.now().time()
        else:
            end_time = self.endTime

        dend = datetime.datetime.combine(datetime.date.today(), end_time)
        dstart = datetime.datetime.combine(datetime.date.today(), self.startTime)
        res = dend-dstart
        return res.total_seconds()

    def working_time(self):
        total_cycle = self.total_cycle_time()
        cycles = self.complete_cycles()
        rest = self.time_elapsed() % total_cycle

        if rest >= self.workCycle.time:
            extra = self.workCycle.time
        else:
            extra = rest

        return cycles * self.workCycle.time + extra

    def not_finished(self):
        return self.endTime is None

    def resting_time(self):
        return self.time_elapsed() - self.working_time()

    def complete_cycles(self):
        total_cycle = self.total_cycle_time()
        return math.floor(self.time_elapsed() / total_cycle)

    def total_cycle_time(self):
        return self.workCycle.time + self.restCycle.time
