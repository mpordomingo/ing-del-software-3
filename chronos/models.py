from django.db import models


class Task(models.Model):
    VALID_STATES = [
        (1, "To Do"),
        (2, "In Progress"),
        (3, "Done")
    ]

    code = models.AutoField(null=False, primary_key=True)
    title = models.CharField(default="", max_length=255)
    description = models.CharField(default="", null=False, max_length=255)
    state = models.CharField(default="To Do", max_length=15, choices=VALID_STATES)

    tasks = models.Manager()

