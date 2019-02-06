from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('professor', 'Professor')
    )
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')
    professor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def user_pre_save_handler(cls, sender, instance, **kwargs):
        if instance.is_superuser and instance.is_staff:
            instance.type = 'admin'


models.signals.pre_save.connect(CustomUser.user_pre_save_handler, sender=CustomUser)
