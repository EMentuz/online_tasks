# Generated by Django 5.0.2 on 2024-04-08 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_task_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.CharField(choices=[('admin', 'admin'), ('admin1', 'admin1'), ('admin2', 'admin2')], max_length=100, verbose_name='Исполнитель'),
        ),
    ]