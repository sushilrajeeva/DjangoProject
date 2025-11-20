from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import UserDetails
from django.views.decorators.csrf import csrf_exempt
import json

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


@csrf_exempt
def get_all_users(request):
    """
    API endpoint to retrieve all users.
    
    Method: GET
    URL: /api/users/
    
    Returns:
        JSON response with list of all users
    """
    if request.method == 'GET':
        try:
            # Get all users from database
            users = UserDetails.objects.all()
            
            # Convert to list of dictionaries
            users_list = []
            for user in users:
                users_list.append({
                    'username': user.username,
                    'email': user.email,
                    'password': user.password
                })
            
            return JsonResponse({
                'success': True,
                'count': len(users_list),
                'data': users_list
            }, status=200)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Method not allowed. Use GET.'
    }, status=405)


@csrf_exempt
def get_user_by_email(request, email):
    """
    API endpoint to retrieve a single user by email.
    
    Method: GET
    URL: /api/users/<email>/
    
    Args:
        email: User's email address
        
    Returns:
        JSON response with user details
    """
    if request.method == 'GET':
        try:
            # Get user by email
            user = UserDetails.objects.get(email=email)
            
            return JsonResponse({
                'success': True,
                'data': {
                    'username': user.username,
                    'email': user.email,
                    'password': user.password
                }
            }, status=200)
            
        except UserDetails.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': f'User with email {email} not found'
            }, status=404)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Method not allowed. Use GET.'
    }, status=405)


@csrf_exempt
def update_user(request, email):
    """
    API endpoint to update user details.
    
    Method: PUT
    URL: /api/users/<email>/update/
    
    Args:
        email: User's email address
        
    Body (JSON):
        {
            "username": "new_username",
            "email": "new_email@example.com",
            "password": "new_password"
        }
        
    Returns:
        JSON response with updated user details
    """
    if request.method == 'PUT':
        try:
            # Get user by email
            user = UserDetails.objects.get(email=email)
            
            data = json.loads(request.body)
            
            # Storing old values
            old_username = user.username
            old_email = user.email
            
            new_username = data.get('username', user.username)
            if new_username != old_username:
                if UserDetails.objects.filter(username=new_username).exists():
                    return JsonResponse({
                        'success': False,
                        'error': 'Username already exists'
                    }, status=400)
            
            # Check if email needs to be updated
            new_email = data.get('email', user.email)
            if new_email != old_email:
                if UserDetails.objects.filter(email=new_email).exists():
                    return JsonResponse({
                        'success': False,
                        'error': 'Email already exists'
                    }, status=400)
            
            new_password = data.get('password', user.password)
            
            # If username is being changed (username is primary key)
            # We need to delete old record and create new one
            if new_username != old_username:
                user.delete()
                
                # Create new user with updated data
                updated_user = UserDetails.objects.create(
                    username=new_username,
                    email=new_email,
                    password=new_password
                )
            else:
                # Just update the existing user
                user.email = new_email
                user.password = new_password
                user.save()
                updated_user = user
            
            return JsonResponse({
                'success': True,
                'message': 'User updated successfully',
                'data': {
                    'username': updated_user.username,
                    'email': updated_user.email,
                    'password': updated_user.password
                }
            }, status=200)
            
        except UserDetails.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': f'User with email {email} not found'
            }, status=404)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON format'
            }, status=400)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Method not allowed. Use PUT.'
    }, status=405)

@csrf_exempt
def delete_user(request, email):
    """
    API endpoint to delete a user by email.
    
    Method: DELETE
    URL: /api/users/<email>/
    
    Args:
        email: User's email address
        
    Returns:
        JSON response confirming deletion
    """
    if request.method == 'DELETE':
        try:
            # Get user by email
            user = UserDetails.objects.get(email=email)
            
            # Store username before deletion
            username = user.username
            
            # Delete user
            user.delete()
            
            return JsonResponse({
                'success': True,
                'message': f'User {username} with email {email} deleted successfully'
            }, status=200)
            
        except UserDetails.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': f'User with email {email} not found'
            }, status=404)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Method not allowed. Use DELETE.'
    }, status=405)

