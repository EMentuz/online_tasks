# Generated by Django 5.0.2 on 2024-04-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.CharField(default='NULL', max_length=100, verbose_name='Исполнитель'),
        ),
    ]