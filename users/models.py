from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets
import string

class User(AbstractUser):
    id = models.CharField(max_length=6, default=''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(6)), primary_key=True)

    

