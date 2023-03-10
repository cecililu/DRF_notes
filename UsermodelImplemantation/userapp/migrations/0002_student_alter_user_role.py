# Generated by Django 4.1.3 on 2023-01-11 03:59

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("userapp.user",),
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("ADMIN", "Admin"),
                    ("STUDENT", "Student"),
                    ("TEACHER", "Teacher"),
                ],
                max_length=50,
            ),
        ),
    ]
