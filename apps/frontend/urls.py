from django.urls import path
from.views import IndexView, EmployeeAddView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', EmployeeAddView.as_view(), name='employee_add'),
]
