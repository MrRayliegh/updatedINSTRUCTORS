# instructors/urls.py
from django.urls import path
from .views import instructor_list, instructor_search, instructor_details, filter_instructors
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', instructor_list, name='instructor_list'),
    path('search/', instructor_search, name='instructor_search'),
    path('details/', instructor_details, name='instructor_details'),  # Ensure this matches your AJAX call
    path('filter/', filter_instructors, name='filter_instructors'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)