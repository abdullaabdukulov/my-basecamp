from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    GENDER = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True, help_text='Format following like this 2023-03-09.')

    def __str__(self):
        return f'Profile of {self.user.username}'
