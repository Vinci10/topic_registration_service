from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('s', 'Student'),
        ('p', 'Professor')
    )
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='s')
    professor = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'