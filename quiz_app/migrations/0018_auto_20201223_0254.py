# Generated by Django 3.1.4 on 2020-12-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0017_auto_20201223_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='time_taken',
            field=models.CharField(max_length=50),
        ),
    ]