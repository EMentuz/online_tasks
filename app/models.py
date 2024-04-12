from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
        ('В ожидании', 'В ожидании'),
        ('В процессе', 'В процессе'),
        ('Завершено', 'Завершено'),
    )

# Получение списка зарегистрированных пользователей
registered_users = User.objects.all()
# Создание CHOICES из списка пользователей
user_choices = [(user.username, user.username) for user in registered_users]

class Task(models.Model):
    # id = models.BigIntegerField(primary_key=True, auto_created=True)
    name = models.CharField(blank=False, null=False, max_length=100, verbose_name="Название", unique=True)
    description = models.TextField(blank=False, null=False, max_length=500, verbose_name="Описание")
    # executor = models.CharField(blank=False, null=False, max_length=100, choices=user_choices, verbose_name="Исполнитель")
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name="Исполнитель")
    status = models.CharField(blank=False, null=False, max_length=10, choices=STATUS_CHOICES)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_of_completion = models.DateTimeField(blank=False, null=False, verbose_name="Дата завершения")


    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.name

class Table_com(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', verbose_name="Задача")
    text = models.TextField(verbose_name="Текст")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="Автор")
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-date_of_creation']

    def __str__(self):
        return self.text
