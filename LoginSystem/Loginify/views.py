from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails
from django.views.decorators.csrf import csrf_exempt

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




@csrf_exempt
def signup_view(request):
    """
    Handle user signup/registration.
    
    GET: Display signup form
    POST: Process signup form and create new user
    
    Args:
        request: HttpRequest object
        
    Returns:
        Rendered signup template or redirect to login page
    """
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validate inputs
        if not username or not email or not password:
            return render(request, 'Loginify/signup.html', {
                'error': 'All fields are required!'
            })
        
        # Check if username already exists
        if UserDetails.objects.filter(username=username).exists():
            return render(request, 'Loginify/signup.html', {
                'error': 'Username already exists!'
            })
        
        # Check if email already exists (unique constraint)
        if UserDetails.objects.filter(email=email).exists():
            return render(request, 'Loginify/signup.html', {
                'error': 'Email already registered!'
            })
        
        # Create new user
        try:
            user = UserDetails(
                username=username,
                email=email,
                password=password
            )
            user.save()
            
            # Redirect to login page after successful signup
            return redirect('login')
            
        except Exception as e:
            return render(request, 'Loginify/signup.html', {
                'error': f'Error creating account: {str(e)}'
            })
    
    # GET request - display signup form
    return render(request, 'Loginify/signup.html')


@csrf_exempt
def login_view(request):
    """
    Handle user login/authentication.
    
    GET: Display login form
    POST: Process login form and authenticate user
    
    Args:
        request: HttpRequest object
        
    Returns:
        Rendered login template or redirect to success page
    """
    if request.method == 'POST':
        # Get form data
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validate inputs
        if not email or not password:
            return render(request, 'Loginify/login.html', {
                'error': 'Email and password are required!'
            })
        
        # Check if user exists and password matches
        try:
            user = UserDetails.objects.get(email=email)
            
            if user.password == password:
                # Login successful - redirect to success page
                return render(request, 'Loginify/success.html', {
                    'username': user.username,
                    'email': user.email
                })
            else:
                # Invalid password
                return render(request, 'Loginify/login.html', {
                    'error': 'Invalid password!'
                })
                
        except UserDetails.DoesNotExist:
            # User not found
            return render(request, 'Loginify/login.html', {
                'error': 'Email not registered!'
            })
    
    # GET request - display login form
    return render(request, 'Loginify/login.html')