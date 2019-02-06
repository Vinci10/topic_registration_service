from django.db import models
from users.models import CustomUser


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=False)
    professor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TopicRegistration(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=False)
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Student: {self.student.first_name} {self.student.last_name} -> topic: {self.topic.name}'


class Timer(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'Start: {self.start_date} --- End: {self.end_date}'

    @classmethod
    def timer_pre_save_handler(cls, sender, instance, **kwargs):
        """During creating new Timer in admin panel set seconds to 00"""
        if instance.end_date < instance.start_date:
            raise ValueError
        Timer.objects.all().delete()


models.signals.pre_save.connect(Timer.timer_pre_save_handler, sender=Timer)
