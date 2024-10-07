# Generated by Django 5.1.1 on 2024-10-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructors", "0003_instructor_department_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="instructor",
            name="profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="instructor_images/"
            ),
        ),
        migrations.AlterField(
            model_name="instructor",
            name="department_type",
            field=models.CharField(
                choices=[
                    ("Not Specified", "Not Specified"),
                    ("COT", "College of Technology"),
                    ("COED", "College of Education"),
                    ("COENG", "College of Engineering"),
                    ("COMGENT", "College of Management and Entrepreneurship"),
                ],
                default="Not Specified",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="instructor",
            name="employment_type",
            field=models.CharField(
                choices=[
                    ("Not Specified", "Not Specified"),
                    ("REGULAR", "Regular"),
                    ("COS", "Contract of Service"),
                ],
                default="Not Specified",
                max_length=15,
            ),
        ),
    ]
