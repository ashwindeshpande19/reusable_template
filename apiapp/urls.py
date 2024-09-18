from django.urls import path
from .views import form_view


# Define the URL patterns for the application
# Map the root URL ('') to the 'form_view' function and name this route 'submit_form'
urlpatterns = [
    path('', form_view, name='submit_form'),  
    # When the user navigates to the root URL (e.g., /), the 'form_view' function will be called
]