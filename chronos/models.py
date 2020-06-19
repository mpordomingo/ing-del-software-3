from django.db import models
from functools import reduce


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