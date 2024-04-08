from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from app.models import Task, Table_com
from app.forms import Table_comForm
from mytasks.forms import ChangeStatusForm


# Create your views here.

def my_tasks(request):
    # print(user)
    user = request.user
    tasks_pr = Task.objects.filter(executor=user, status='В процессе').order_by('-date_of_creation')
    tasks_await = Task.objects.filter(executor=user, status='В ожидании').order_by('-date_of_creation')
    tasks_done = Task.objects.filter(executor=user, status='Завершено').order_by('-date_of_creation')

    return render(request, 'my_tasks.html',
                  {'tasks_pr': tasks_pr, 'tasks_await': tasks_await, 'tasks_done': tasks_done})

def my_task_detail(request, task_id):
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
            return render(request, 'my_task_detail.html', {'task': task, 'comments': comments, 'form': form})
    else:
        form = Table_comForm()
    return render(request, 'my_task_detail.html', {'task': task, 'comments': comments, 'form': form})


def change_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = ChangeStatusForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        # return redirect('my_task_detail', task_id=task_id)
        return redirect('my_tasks')

    return render(request, 'change_status.html', {'form': form, 'task': task})