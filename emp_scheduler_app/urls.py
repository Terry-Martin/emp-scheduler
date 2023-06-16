from django.urls import path
from .views import HomeView, InfoView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('emp_info/<int:pk>', InfoView.as_view(), name='emp_info'),
]
