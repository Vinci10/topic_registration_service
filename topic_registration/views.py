from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Timer
from .services import register_user_topic, is_topic_occupied, is_registration_open
from .exceptions import NoStudentError, OccupiedTopicError, RegistrationClosedError
from django.contrib import messages


@login_required(login_url='/users/login/')
def topic_registration(request):
    topic_name_list = []
    for topic in Topic.objects.filter(professor=request.user.professor):
        occupied, by_current_user = is_topic_occupied(request.user, topic)
        topic_name_list.append((topic.name, occupied, by_current_user))
    timer = Timer.objects.first()
    context = {
        'topic_name_list': topic_name_list,
        'start_date': timer.start_date.strftime("%Y-%m-%d %H:%M"),
        'end_date': timer.end_date.strftime("%Y-%m-%d %H:%M")
    }
    return render(request, 'topic_registration/topic_registration.html', context)


@login_required(login_url='/users/login/')
def topic_register(request):
    try:
        if not is_registration_open():
            raise RegistrationClosedError
        selected_topic = request.POST['topic']
        register_user_topic(request.user, selected_topic)
        messages.success(request, 'Rejestracja zakonczona pomyslnie')
    except KeyError:
        messages.error(request, 'Nie wybrano tematu')
    except NoStudentError:
        messages.error(request, 'Tylko student moze zarejestrowac temat')
    except OccupiedTopicError:
        messages.error(request, 'Wybrany temat jest juz zarezerwowany')
    except RegistrationClosedError:
        messages.error(request, 'Rejestracja jest zamknieta')
    except Exception:
        messages.error(request, 'Nieoczekiwany blad')
    return redirect('topic_registration:topic_registration')
