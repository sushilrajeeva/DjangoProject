# Django Shell Commands - Task 4

## Overview
This document contains all Django shell commands tested for Task 4.

## Prerequisites
```bash
# Activate virtual environment
source ../DjangoAssignment/bin/activate

# Navigate to project directory
cd LoginSystem

# Open Django shell
python3 manage.py shell
```

## Import Model
```python
from Loginify.models import UserDetails
```

---

## CRUD Operations

### 1. Create a New User
```python
new_user = UserDetails.objects.create(
    username="example_user",
    email="user@example.com",
    password="example123"
)
print(f"Created: {new_user.username}")
```

**Expected Output:** `Created: example_user`

---

### 2. Retrieve All Users
```python
all_users = UserDetails.objects.all()
for user in all_users:
    print(f"Username: {user.username}, Email: {user.email}")
```

**Expected Output:**
```
Username: example_user, Email: user@example.com
Username: admin, Email: admin@example.com
...
```

---

### 3. Retrieve Single User by Username
```python
username = "example_user"
user_by_name = UserDetails.objects.get(username=username)
print(f"Found: {user_by_name.username} - {user_by_name.email}")
```

**Expected Output:** `Found: example_user - user@example.com`

---

### 4. Update a User
```python
user = UserDetails.objects.get(username="example_user")
user.email = "updated@example.com"
user.save()
print(f"Updated email: {user.email}")
```

**Expected Output:** `Updated email: updated@example.com`

---

### 5. Filter/Query Users
```python
# Filter by email containing "example"
queryset = UserDetails.objects.filter(email__contains="example")
for user in queryset:
    print(f"{user.username}: {user.email}")

# Filter by specific username
user = UserDetails.objects.filter(username="admin").first()
print(f"Admin user: {user}")
```

---

### 6. Delete a User
```python
username_to_delete = "example_user"
user_to_delete = UserDetails.objects.get(username=username_to_delete)
print(f"Deleting: {user_to_delete.username}")
user_to_delete.delete()

# Verify deletion
try:
    UserDetails.objects.get(username=username_to_delete)
except UserDetails.DoesNotExist:
    print("User successfully deleted!")
```

**Expected Output:**
```
Deleting: example_user
User successfully deleted!
```

---

## Additional Useful Commands

### Count Total Users
```python
count = UserDetails.objects.count()
print(f"Total users: {count}")
```

### Check if User Exists
```python
exists = UserDetails.objects.filter(username="admin").exists()
print(f"Admin exists: {exists}")
```

### Get or Create User
```python
user, created = UserDetails.objects.get_or_create(
    username="test_user",
    defaults={'email': 'test@example.com', 'password': 'test123'}
)
print(f"User: {user.username}, Created: {created}")
```

### Order Users
```python
# Order by username alphabetically
users = UserDetails.objects.all().order_by('username')
for user in users:
    print(user.username)

# Order by username descending
users = UserDetails.objects.all().order_by('-username')
```

### Bulk Create Users
```python
users_to_create = [
    UserDetails(username=f"user{i}", email=f"user{i}@example.com", password="pass123")
    for i in range(1, 6)
]
UserDetails.objects.bulk_create(users_to_create)
print(f"Created {len(users_to_create)} users")
```

---

## Exit Shell
```python
exit()
```

---
