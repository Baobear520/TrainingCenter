# Generated by Django 4.1.2 on 2023-02-24 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0006_enrollment_lessons"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enrollment",
            name="lessons",
            field=models.IntegerField(verbose_name="Number_of_lessons_left"),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="money_paid",
            field=models.DecimalField(
                decimal_places=1, max_digits=7, verbose_name="Payment"
            ),
        ),
    ]