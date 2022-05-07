from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class User(AbstractUser):
	username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
	email = models.EmailField(max_length = 120, unique = True)
	phone_no = models.CharField(max_length = 15)
	date_joined = models.DateField(auto_now_add=True)
	is_librarian = models.BooleanField(default=False)
	is_member = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
	
	def __str__(self):
		return str(self.email)
    
