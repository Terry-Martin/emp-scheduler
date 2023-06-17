from django.urls import path
from .views import HomeView, InfoView, AddNewEmployeeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('emp_info/<int:pk>', InfoView.as_view(), name='emp_info'),
    path('add_new_employee/', AddNewEmployeeView.as_view(),
         name='add_new_employee'),
]
