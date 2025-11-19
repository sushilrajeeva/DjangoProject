from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    """
    This is a test view that returns 'Hello, world!' message.
    
    Args / input:
        request: HttpRequest object
        
    Returns:
        HttpResponse with 'Hello, world!' message
    """
    return HttpResponse('Hello, world!')