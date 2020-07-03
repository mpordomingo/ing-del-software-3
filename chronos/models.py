from django.db import models
import datetime


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

    def finalize(self):
        assert self.state == "In Progress", "La tarea debe estar en estado 'In Progress'"
        self.state = "Done"

    def start(self):
        assert self.state == "To Do", "La tarea debe estar en estado 'To Do'"
        self.state = "In Progress"


class Cycle(models.Model):
    totalTime = models.FloatField(null=True)


class WorkCycle(Cycle):
    time = models.FloatField(default=25)


class RestCycle(Cycle):
    time = models.FloatField(default=5)


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
        self.startTime = datetime.now().time()

    def stop(self):
        assert self.endTime is None, "Este registro de tiempo ya fue finalizado."
        self.endTime = datetime.now().time()

    def ustop(self):
        if self.endTime is None:
            self.endTime = datetime.now().time()

    def time_elapsed(self):
        if (self.endTime is None) and (self.startTime is None):
            return 0

        dend = datetime.datetime.combine(datetime.date.today(), self.endTime)
        dstart = datetime.datetime.combine(datetime.date.today(), self.startTime)
        res = dend-dstart
        return res.total_seconds()

    def working_time(self):
        total = self.time_elapsed()
        totalCycle = self.restCycle.time + self.workCycle.time
        ratio = self.workCycle.time / totalCycle
        return total * ratio

    def resting_time(self):
        total = self.timeElapsed()
        totalCycle = self.restCycle.time + self.workCycle.time
        ratio = self.restCycle.time / totalCycle
        return total * ratio
