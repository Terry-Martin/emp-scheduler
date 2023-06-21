from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Shift(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    break_one = models.CharField(max_length=200)
    break_two = models.CharField(max_length=200)
    emp_detail = models.ManyToManyField('Emp_Details', through='Scheduled')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    
    def __str__(self):
        return self.name


class Emp_Details(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    name_tag = models.CharField(max_length=200)
    weekly_contact_hours = models.FloatField(default=40)
    department = models.CharField(max_length=200)
    supervisor = models.CharField(max_length=200, default="Boss")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shifts = models.ManyToManyField('Shift', through='Scheduled')

    # Check on_delete options
    # shift = models.ForeignKey(
    #     Shift, blank=True, null=True, on_delete=models.CASCADE, default="")
    # shift = models.ManyToManyField(
    #     Shift, blank=True, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('home')

# Connector/Many-To-Many model between Shift model and Emp_Details model
class Scheduled(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    emp_detail = models.ForeignKey(Emp_Details, on_delete=models.CASCADE)

    def __str__(self):
        return self.shift
