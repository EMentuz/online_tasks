from django.urls import path, include
# from app.views import main, login, ReqisterUser
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('register/', register, name='register'),
    # path('profile', profile_view, name='profile'),
    path('task/<int:task_id>/', task_detail, name='task_detail'),

    # path('login/', login, name='login'),
    # path('register/', RegisterUser.as_view(), name='register'),
]
