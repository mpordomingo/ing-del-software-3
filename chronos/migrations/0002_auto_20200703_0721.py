# Generated by Django 3.0.7 on 2020-07-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerecord',
            name='endTime',
            field=models.TimeField(null=True),
        ),
    ]
