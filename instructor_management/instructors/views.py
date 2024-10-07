# instructors/views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Instructor
from django.db.models import Q

DEFAULT_IMAGE_URL = '/static/images/default_profile.png'  # Adjust the path based on your project structure

def instructor_list(request):
    query = request.GET.get('q', '')
    filter_type = request.GET.get('filter', 'ALL')  # Employment Type
    department_filter = request.GET.get('department', 'ALL')  # Department Type

    # Start with all instructors
    instructors = Instructor.objects.all()

    # Apply filtering logic
    if filter_type == 'REGULAR':
        instructors = instructors.filter(employment_type='REGULAR')
    elif filter_type == 'COS':
        instructors = instructors.filter(employment_type='COS')
    # If filter_type is 'ALL', do nothing (show all instructors)

    if department_filter == 'COT':
        instructors = instructors.filter(department_type='COT')
    elif department_filter == 'COED':
        instructors = instructors.filter(department_type='COED')
    elif department_filter == 'COENG':
        instructors = instructors.filter(department_type='COENG')
    elif department_filter == 'COMGENT':
        instructors = instructors.filter(department_type='COMGENT')
    # If department_filter is 'ALL', do nothing (show all instructors)

    # Apply search query
    if query:
        instructors = instructors.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query)
        )
        

    return render(request, 'instructors/instructor_list.html', {
        'instructors': instructors,
        'filter': filter_type,
        'department': department_filter,
        'query': query,  # Pass the search query to the template
    })


def instructor_search(request):
    query = request.GET.get('q', '')
    filter_type = request.GET.get('filter', 'ALL')  # Employment Type
    department_filter = request.GET.get('department', 'ALL')  # Department Type

    # Start with all instructors
    results = Instructor.objects.all()

    # Apply filtering logic for employment type
    if filter_type == 'REGULAR':
        results = results.filter(employment_type='REGULAR')
    elif filter_type == 'COS':
        results = results.filter(employment_type='COS')
    
    # Apply filtering logic for department type
    if department_filter == 'COT':
        results = results.filter(department_type='COT')
    elif department_filter == 'COED':
        results = results.filter(department_type='COED')
    elif department_filter == 'COENG':
        results = results.filter(department_type='COENG')
    elif department_filter == 'COMGENT':
        results = results.filter(department_type='COMGENT')

    # Apply search query
    if query:
        results = results.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query)
        )

    suggestions = [
        {
            'id': instructor.id,
            'name': f"{instructor.first_name} {instructor.last_name}",  # Added space between first and last names
            'image': instructor.profile_image.url if instructor.profile_image else DEFAULT_IMAGE_URL
        }
        for instructor in results
    ]
    
    return JsonResponse({'results': suggestions})   


def instructor_details(request):
    instructor_id = request.GET.get('id')
    instructor = get_object_or_404(Instructor, id=instructor_id)
    
    # Create a response with default image handling and correct formatting
    data = {
        'html': (
            "<div style='position: relative;'>"  # Wrapper for positioning
            f"<h3>{instructor.first_name} {instructor.last_name}</h3>"  # Added space between names
            f"<img src='{instructor.profile_image.url if instructor.profile_image else DEFAULT_IMAGE_URL}' alt='Profile Image' width='100' style='position: absolute; top: 0; right: 0;'>"  # Position image at top right
            f"<p>Employment Type: {instructor.employment_type}</p>"
            f"<p>Department Type: {instructor.department_type}</p>"
            f"<p>Qualified Courses: {', '.join(instructor.qualified_course)}</p>"
            f"<p>Availability Days: {instructor.availability_days}</p>"
            f"<p>Availability Times: {instructor.availability_times}</p>"
            "</div>"
        )
    }
    return JsonResponse(data)

def filter_instructors(request):
    # Logic for filtering instructors can be added here
    return render(request, 'instructors/instructor_filter.html')
