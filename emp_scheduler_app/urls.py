from django.urls import path
from .views import HomeView, InfoView, AddNewEmployeeView, AddScheduleView, ShiftView, ScheduleView, DepartmentView, ManagerView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('emp_info/<int:pk>', InfoView.as_view(), name='emp_info'),
    path('add_new_employee/', AddNewEmployeeView.as_view(),
         name='add_new_employee'),
    path('add_schedule/', AddScheduleView.as_view(),
         name='add_schedule'),
    path('shift_info/', ShiftView.as_view(), name="shift_info"),
    path('schedule_info/', ScheduleView.as_view(), name="schedule_info"),
    path('department_info/', DepartmentView.as_view(), name="department_info"),
    path('manager_info/', ManagerView.as_view(), name="manager_info"),
]
