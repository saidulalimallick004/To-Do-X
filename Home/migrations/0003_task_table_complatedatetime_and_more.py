# Generated by Django 5.1.6 on 2025-02-24 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_task_table_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_table',
            name='ComplateDateTime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task_table',
            name='DeadlineTime',
            field=models.TimeField(),
        ),
    ]
