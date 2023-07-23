from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Emp_Details, Shift, Scheduled, Department, Manager


class HomeView(ListView):
    model = Emp_Details
    template_name = 'home.html'
    ordering = ['-created_at']

    # Add test filter
    # queryset = Emp_Details.objects.filter(weekly_contact_hours=40)
    # queryset = Emp_Details.objects.filter(first_name='Mary')


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

    ordering = ['id']


class ScheduleView(ListView):
    model = Scheduled
    template_name = 'schedule_info.html'


class DepartmentView(ListView):
    model = Department
    template_name = 'department_info.html'


class ManagerView(ListView):
    model = Manager
    template_name = 'manager_info.html'
