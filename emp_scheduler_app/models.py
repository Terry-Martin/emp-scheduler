from django.db import models
from django.contrib.auth.models import User


class Emp_Details(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
