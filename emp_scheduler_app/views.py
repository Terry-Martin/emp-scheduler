from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Emp_Details, Shift, Scheduled


class HomeView(ListView):
    model = Emp_Details
    template_name = 'home.html'
    ordering = ['-created_at']


class InfoView(DetailView):
    model = Emp_Details
    template_name = 'emp_info.html'


class AddNewEmployeeView(CreateView):
    model = Emp_Details
    template_name = 'add_new_employee.html'
    # add all fields from model
    fields = '__all__'  # add all fields from model
    # select certain fields
    # fields = ('first_name', 'department', 'supervisor')


class AddScheduleView(CreateView):
    model = Shift
    template_name = 'add_schedule.html'
    fields = '__all__'


class ShiftView(ListView):
    model = Shift
    template_name = 'shift_info.html'


class ScheduleView(ListView):
    model = Scheduled
    template_name = 'schedule_info.html'
