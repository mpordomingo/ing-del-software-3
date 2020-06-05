from django.db import models


class Task(models.Model):
    code = models.AutoField(null=False, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    state = models.CharField(max_length=10)
    assigneeId = models.IntegerField(default=0)
    projectId = models.IntegerField(default=1, null=False)

    tasks = models.Manager()

    def description(self):
        return self.description

    def code(self):
        return self.code

    def state(self):
        return self.state
