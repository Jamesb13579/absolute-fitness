from django.shortcuts import render
from .models import Trainers, Gym, Classes


def trainers(request):
    """ a view to return trainer information"""

    trainers = Trainers.objects.all()

    context = {
        'trainers': trainers,
    }

    return render(request, 'about/meet_our_trainers.html', context)


def gym(request):
    """ a view to return gym information"""

    gym = Gym.objects.all()

    context = {
        'gym': gym,
    }

    return render(request, 'about/our_gym.html', context)


def classes(request):
    """ a view to return classes information and times"""

    classes = Classes.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'about/classes.html', context)
