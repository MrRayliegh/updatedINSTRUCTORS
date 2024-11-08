# Generated by Django 5.1.1 on 2024-10-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructors", "0002_alter_instructor_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="instructor",
            name="department_type",
            field=models.CharField(
                choices=[
                    ("COT", "College of Technology"),
                    ("COED", "College of Education"),
                    ("COENG", "College of Engineering"),
                    ("COMGENT", "College of Management and Entrepreneurship"),
                    ("Not Specified", "Not Specified"),
                ],
                default="Not Specified",
                max_length=20,
            ),
        ),
    ]
