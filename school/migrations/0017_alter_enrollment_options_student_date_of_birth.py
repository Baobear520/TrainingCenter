# Generated by Django 4.1.2 on 2023-04-07 00:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0016_alter_student_photo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="enrollment", options={"ordering": ("date_enrolled",)},
        ),
        migrations.AddField(
            model_name="student",
            name="date_of_birth",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]