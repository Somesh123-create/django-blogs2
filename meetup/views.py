from django.shortcuts import render, redirect
from .models import MeetUp, Participant
from .forms import RegistrationForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse



def index(request):
    meetups = MeetUp.objects.all()
    return render(request, 'meetup/index.html', {'meetups':meetups})


def meetup_detail(request, slug):
    try:
        meetups = get_object_or_404(MeetUp, slug=slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                meetups.participants.add(participant)
                return redirect('meetup:register_success', slug=slug)
        return render(request, 'meetup/meetup_detail.html', {'meetups':meetups, 'meetup_found': True, 'form':registration_form})

    except Exception as exc:
        return render(request, 'meetup/meetup_detail.html', {'meetup_found': False})


def register_success(request, slug):
    meetup = MeetUp.objects.get(slug=slug)
    return render(request, 'meetup/registration_success.html', {'meetup':meetup})
