from .exceptions import NoStudentError, OccupiedTopicError
from django.db import IntegrityError, transaction
from .models import TopicRegistration, Topic, Timer
from datetime import datetime


def delete_user_topic(user):
    registration = TopicRegistration.objects.get(student=user)
    registration.delete()


def is_topic_occupied(student, topic):
    t = TopicRegistration.objects.filter(topic=topic)
    if t.count():
        return True, bool(t.filter(student=student).count())
    return False, False


@transaction.atomic
def register_user_topic(user, topic_name):
    if user.type != 'student':
        raise NoStudentError
    topic = Topic.objects.get(professor=user.professor, name=topic_name)
    if is_topic_occupied(user, topic)[0]:
        raise OccupiedTopicError
    try:
        if TopicRegistration.objects.filter(student=user).count():
            delete_user_topic(user)
        registration = TopicRegistration(student=user, topic=topic)
        registration.save()
    except IntegrityError:
        raise OccupiedTopicError


def is_registration_open():
    timer = Timer.objects.first()
    return timer.start_date <= datetime.now() <= timer.end_date
