from django import forms
from django.contrib import admin
from .models import Instructor
from django.forms.widgets import TimeInput

class TimePickerWidget(TimeInput):
    input_type = 'time'

class InstructorForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False, help_text='Upload a profile picture.', widget=forms.ClearableFileInput)

    qualified_course = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter courses separated by commas'}),
        help_text='Enter courses separated by commas (e.g., "AST, FOLA, PROGRAMMING").',
    )
    
    class Meta:
        model = Instructor
        fields = '__all__'
        widgets = {
            'availability_times': TimePickerWidget(format='%H:%M'),
        }

    def clean(self):
        cleaned_data = super().clean()

        # Validate required fields
        if not cleaned_data.get('first_name'):
            self.add_error('first_name', 'This field should not be empty.')
        if not cleaned_data.get('last_name'):
            self.add_error('last_name', 'This field should not be empty.')
        if not cleaned_data.get('employment_type'):
            self.add_error('employment_type', 'This field should not be empty.')
        if not cleaned_data.get('department_type'):
            self.add_error('department_type', 'This field should not be empty.')

        qualified_courses = cleaned_data.get('qualified_course', '')
        if qualified_courses:
            cleaned_data['qualified_course'] = [course.strip() for course in qualified_courses.split(',')]

class InstructorAdmin(admin.ModelAdmin):
    form = InstructorForm

    list_display = ('first_name', 'middle_name', 'last_name', 'employment_type')
    search_fields = ('first_name', 'middle_name', 'last_name', 'employment_type')
    list_filter = ('employment_type','department_type')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'middle_name', 'last_name', 'employment_type', 'department_type', 'qualified_course', 'availability_days', 'availability_times')
        }),
    )
    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/jquery-timepicker/1.13.18/jquery.timepicker.min.css',
            )
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/jquery-timepicker/1.13.18/jquery.timepicker.min.js',
        )


admin.site.site_header = "CTU Dumanug Extension Campus"
admin.site.site_title = "CTU-DEx"
admin.site.index_title = "Welcome to My Admin Pannel"

# Register the updated admin class
admin.site.register(Instructor, InstructorAdmin)

