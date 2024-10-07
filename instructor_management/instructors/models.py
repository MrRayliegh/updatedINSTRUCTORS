from django.db import models
from datetime import date, time

class Instructor(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('Not Specified', 'Not Specified'),  # Add "Not Specified" as a choice
        ('REGULAR', 'Regular'),
        ('COS', 'Contract of Service')
    ]

    DEPARTMENT_TYPE_CHOICES = [
        ('Not Specified', 'Not Specified'),  # Add "Not Specified" as a choice
        ('COT', 'College of Technology'),
        ('COED', 'College of Education'),
        ('COENG', 'College of Engineering'),
        ('COMGENT', 'College of Management and Entrepreneurship')
    ]

    # Instructor details
    first_name = models.CharField(max_length=100, blank=False)  # First name is required
    middle_name = models.CharField(max_length=255, blank=True, null=True)  # Optional field
    last_name = models.CharField(max_length=100, blank=False)  # Last name is required

    # Employment and department type fields
    employment_type = models.CharField(
        max_length=15,
        choices=EMPLOYMENT_TYPE_CHOICES,
        blank=False,
        null=False,
        default='Not Specified'  # Default to 'Not Specified' for existing rows
    )
    
    department_type = models.CharField(
        max_length=20,
        choices=DEPARTMENT_TYPE_CHOICES,
        blank=False,
        null=False,
        default='Not Specified'
    )

    # Qualified courses (JSON field)
    qualified_course = models.JSONField(default=list)  # Default to an empty list for qualified courses

    # Availability
    availability_days = models.DateField(default=date.today)  # Default to today's date
    availability_times = models.TimeField(default=time(0, 0))  # Default to midnight as an example
    profile_image = models.ImageField(upload_to='instructor_images/', blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'instructors'  # Specify the exact table name
