from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Emp_Details


class HomeView(ListView):
    model = Emp_Details
    template_name = 'home.html'


class InfoView(DetailView):
    model = Emp_Details
    template_name = 'emp_info.html'


class AddNewEmployeeView(CreateView):
    model = Emp_Details
    template_name = 'add_new_employee.html'
    fields = '__all__'  # add all fields from model
