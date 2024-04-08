from django.urls import path
from .views import *

urlpatterns = [
    path('my_tasks/', my_tasks, name='my_tasks'),
    path('my_task/<int:task_id>/', my_task_detail, name='my_task_detail'),
    path('my_task/<int:task_id>/change_status/', change_status, name='change_status'),



    # path('task/<int:task_id>/', task_detail, name='my_task_detail'),

]
