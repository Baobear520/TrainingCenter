# Generated by Django 4.1.2 on 2023-04-13 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student", options={"ordering": ["user__last_name"]},
        ),
        migrations.RemoveField(model_name="student", name="date_registered",),
    ]