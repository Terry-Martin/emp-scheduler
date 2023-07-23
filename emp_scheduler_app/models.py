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
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "  " + self.start_time

    # class Meta:
    #     ordering = ['start_time']


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Emp_Details(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    name_tag = models.CharField(max_length=200)
    weekly_contact_hours = models.FloatField(default=40)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE)
    # supervisor = models.CharField(max_length=200)
    Manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    # manager = models.CharField(max_length=200)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shifts = models.ManyToManyField('Shift', through='Scheduled')

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ['last_name', 'first_name', 'department']


# Connector/Many-To-Many model between Shift model and Emp_Details model
class Scheduled(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    emp_detail = models.ForeignKey(Emp_Details, on_delete=models.CASCADE)
    schedule_date = models.DateTimeField(default=datetime.now, blank=True)
    schedule_date_day = models.DateTimeField(default=datetime.now, blank=True)
    schedule_date_select = models.DateField(default=date.today)

    def __str__(self):
        return self.shift.start_time + " - " + self.emp_detail.first_name

    class Meta:
        ordering = ['shift', 'emp_detail']
