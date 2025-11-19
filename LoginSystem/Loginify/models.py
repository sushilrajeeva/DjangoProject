from django.db import models

# Create your models here.

class UserDetails(models.Model):
    """
    This UserDetails Model is used to store user registration and login details.
    
    Fields:
        username: Primary key, unique identifier for user
        email: Unique email address for user
        password: User password (max 12 characters)
    """
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12, blank=True)
    
    class Meta:
        verbose_name = "User Detail"
        verbose_name_plural = "User Details"
    
    def __str__(self):
        """String representation of UserDetails object"""
        return self.username