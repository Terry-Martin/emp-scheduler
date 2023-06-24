from django.contrib import admin
from .models import Emp_Details, Shift, Scheduled, Department, Manager

admin.site.register(Emp_Details)
admin.site.register(Shift)
admin.site.register(Scheduled)
admin.site.register(Department)
admin.site.register(Manager)

