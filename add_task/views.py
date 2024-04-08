from django.shortcuts import render, redirect
from add_task.forms import MyForm
# Create your views here.


def add_task(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # добавление в бд
            form.save()
            messages = 'Задача успешно добавлена'
            return render(request, 'add_task.html', {'message': messages})
            # return redirect('main')

    else:
        form = MyForm()
    return render(request, 'add_task.html', {'form': form})