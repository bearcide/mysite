from django.shortcuts import render

from django.shortcuts import render
from .models import Section

def display_content(request):
    # Get all sections with their related points and bulletpoints
    sections = Section.objects.prefetch_related(
        'points', 
        'points__bulletpoints'
    ).all()
    
    return render(request, 'content_display.html', {'sections': sections})
