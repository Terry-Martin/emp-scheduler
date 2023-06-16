from django.db import models
from django.contrib.auth.models import User


class Emp_Details(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    weekly_contact_hours = models.FloatField(default=40)
    department = models.CharField(max_length=200)
    supervisor = models.CharField(max_length=200, default="Boss")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
