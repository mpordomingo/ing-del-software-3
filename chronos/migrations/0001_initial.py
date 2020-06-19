# Generated by Django 3.0.7 on 2020-06-05 19:54

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=255)),
                ('assigneeId', models.IntegerField(default=0)),
                ('projectId', models.IntegerField(default=1)),
                ('state', models.CharField(choices=[(1, 'To Do'), (2, 'In Progress'), (3, 'Blocked'), (4, 'Done')], default='To Do', max_length=15)),
            ],
            managers=[
                ('tasks', django.db.models.manager.Manager()),
            ],
        ),
    ]