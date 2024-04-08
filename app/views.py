from django.shortcuts import render, get_object_or_404
from app.models import Task, Table_com
from .forms import UserRegistrationForm
from app.forms import Table_comForm



# Create your views here.

def main(request):
    tasks_pr = Task.objects.filter(status='В процессе').order_by('-date_of_creation')
    tasks_await = Task.objects.filter(status='В ожидании').order_by('-date_of_creation')
    tasks_done = Task.objects.filter(status='Завершено').order_by('-date_of_creation')

    return render(request, 'main.html', {'tasks_pr': tasks_pr, 'tasks_await':tasks_await, 'tasks_done':tasks_done})


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def task_detail(request, task_id):
    form = Table_comForm()
    task = get_object_or_404(Task, pk=task_id)
    comments = Table_com.objects.filter(task=task)  # Получаем комментарии, связанные с задачей
    if request.method == 'POST':
        form = Table_comForm(request.POST)
        if form.is_valid():
            # добавление в бд
            comment = form.save(commit=False)
            comment.task = task  # Установите поле task для комментария
            comment.user = request.user  # Установите пользователя текущего запроса
            comment.save()
            # После успешного сохранения, создаем новую пустую форму
            form = Table_comForm()
            return render(request, 'task_detail.html', {'task': task, 'comments': comments, 'form': form})
    else:
        form = Table_comForm()
    return render(request, 'task_detail.html', {'task': task, 'comments': comments, 'form': form})

