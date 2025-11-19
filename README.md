# Login System - Django Project

A robust Django-based authentication system with user signup, login, and profile management capabilities.

## Project Description

This Django project creates a comprehensive user management system featuring:
- User registration and authentication
- User profile management
- CRUD operations for user data
- Secure login/logout functionality
- Profile updates and account deletion

The project follows the Django best practices and utilizes Django's built-in features for models, views, URL routing, and template rendering.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Create Virtual Environment
```bash
# Create virtual environment
python -m venv DjangoAssignment
```

### 2. Activate Virtual Environment


**macOS:**
```bash
source DjangoAssignment/bin/activate
```

### 3. Install Django
```bash
pip install django
```

### 4. Run Development Server
```bash
cd LoginSystem
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

## Technology Stack

- **Framework:** Django 5.1.6
- **Language:** Python 3.x

## Project Status

# Task 1: Project Setup Complete
- Virtual environment created
- Django installed
- Project "LoginSystem" created
- Application "Loginify" created and registered

<img width="1913" height="936" alt="Screenshot 2025-11-19 at 5 47 37 AM" src="https://github.com/user-attachments/assets/8df087f6-d3aa-4ea7-a7e6-889e9dd0eb31" />

# Task 2: 
### Microtask 1: Create Views
- [x] Created `hello_world` view in `Loginify/views.py`
- [x] Returns HttpResponse with "Hello, world!" message
- [x] Added proper documentation to the view function

### Microtask 2: Define URL Patterns
- [x] Created `Loginify/urls.py` with URL patterns
- [x] Mapped root URL ('') to hello_world view
- [x] Updated project-level `LoginSystem/urls.py` to include Loginify URLs

## Testing
- [x] Server runs without errors
- [x] Endpoint accessible at `http://127.0.0.1:8000/`
- [x] Returns "Hello, world!" message correctly


## Screenshots
<img width="369" height="161" alt="Screenshot 2025-11-19 at 6 05 27 AM" src="https://github.com/user-attachments/assets/4c18c74c-14aa-42e3-befe-13482a78f9de" />

## Task 3: Define Models and Authentication System

In this task, I created a complete user authentication system with database models, views, and beautiful HTML templates.

**Microtask 1: Create UserDetails Model**
- Created `UserDetails` model to store user information in database
- Fields: `username` (primary key), `email` (unique), `password`
- Registered model in Django admin panel for easy management
- Created and applied database migrations

**Microtask 2: Define URLs and Templates**
- Created three HTML templates with modern, responsive design:
  - `signup.html` - User registration form
  - `login.html` - User login form
  - `success.html` - Post-login success page
- Defined URL patterns: `/signup/` and `/login/`
- Used Django template language with `{% csrf_token %}` for security

**Microtask 3: Implement Signup View**
- Validates all required fields
- Checks username uniqueness
- Enforces email uniqueness (database constraint)
- Creates new user record
- Redirects to login page after successful registration
- Displays error messages for validation failures

**Microtask 4: Implement Login View**
- Verifies email exists in database
- Validates password matches stored password
- Displays success page with user details on successful login
- Shows appropriate error messages for invalid credentials

### User Flow
```
1. User visits /signup/
   ↓
2. Fills in username, email, password
   ↓
3. Form validates (unique email/username)
   ↓
4. User created in database
   ↓
5. Redirects to /login/
   ↓
6. User enters email and password
   ↓
7. Credentials verified
   ↓
8. Success page displays user info
```

### Key Features

**Form Validation**: All inputs validated before processing  
**Unique Constraints**: Email and username must be unique  
**Error Handling**: User-friendly error messages  
**Responsive Design**: Templates work on all screen sizes  
**Secure Forms**: CSRF protection enabled  
**User Feedback**: Success/error messages displayed clearly  

1. Signup page
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 6 39 36 AM" src="https://github.com/user-attachments/assets/13818617-7949-4ec5-98b7-e0aaaf068bd1" />

2. Login page
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 6 39 48 AM" src="https://github.com/user-attachments/assets/550e6b03-82a3-431f-9937-23cf171f8660" />

3. Success page
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 6 41 43 AM" src="https://github.com/user-attachments/assets/9cb0c2e9-76fe-4d12-b1fc-b31d5c86b56d" />

4. Error messages
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 6 42 18 AM" src="https://github.com/user-attachments/assets/708ac8b9-2bcf-43c9-b80f-9c0e4682173b" />
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 6 42 53 AM" src="https://github.com/user-attachments/assets/67baeb12-48a2-406a-8761-fef5d9e79982" />


5. Admin panel showing UserDetails]
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 6 50 29 AM" src="https://github.com/user-attachments/assets/e23c989e-1d49-4955-a85e-1f85dcd4840c" />

## Task 4: Setup Superuser and Django Admin

In this task, I set up Django's admin interface and explored database operations through the Django shell.

**Create Superuser**
- Created an admin user using `python3 manage.py createsuperuser`
- Credentials: username, email, password
- Allows access to Django admin panel at `/admin/`

**Verify Admin Interface**
- Logged into Django admin successfully
- UserDetails model registered and visible in admin
- Tested CRUD operations through admin UI
- Verified search and filter functionality

**Django Shell Exploration**
- Tested all database operations via `python3 manage.py shell`
- Performed CRUD operations on UserDetails model
- Documented all commands with expected outputs

 1. Admin login page
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 6 50 29 AM" src="https://github.com/user-attachments/assets/1a60df92-41bd-49df-b98e-58a58e8155c4" />

2. Admin dashboard
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 7 18 43 AM" src="https://github.com/user-attachments/assets/2d00a1b5-6a61-4726-8838-fb60d790735e" />

3. UserDetails list in admin
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 7 19 50 AM" src="https://github.com/user-attachments/assets/d228cb8f-4cdd-4748-9750-6dd170138322" />

4
<img width="1136" height="866" alt="Screenshot 2025-11-19 at 7 41 13 AM" src="https://github.com/user-attachments/assets/e446f526-c870-46e2-b85c-183ea9dde0ad" />
<img width="1136" height="866" alt="Screenshot 2025-11-19 at 7 41 20 AM" src="https://github.com/user-attachments/assets/f8e35a71-c801-4d5d-bd0a-09c2ee72c0e5" />
<img width="1136" height="866" alt="Screenshot 2025-11-19 at 7 41 27 AM" src="https://github.com/user-attachments/assets/40432903-0c39-41c1-9267-7024ce8c6db1" />
<img width="1136" height="866" alt="Screenshot 2025-11-19 at 7 41 32 AM" src="https://github.com/user-attachments/assets/7e003dac-a65d-4c6d-8fe1-678d3e95e51f" />
. Shell commands execution

5 User creation in admin
<img width="1909" height="711" alt="Screenshot 2025-11-19 at 7 20 31 AM" src="https://github.com/user-attachments/assets/fa140a8c-d3fa-4d51-8736-a1c1663b7e0f" />

