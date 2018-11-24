from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django import views
from .forms import (
    RegistrationForm,
    EditProfileForm
)
from django.core.mail import send_mail


def home(request):
    return render(request, 'main/home.html')


def membership(request):
    return render(request, 'main/membership.html')


def scheduling(request):
    return render(request, 'main/scheduling.html')


def events(request):
    return render(request, 'main/events.html')


def contact(request):
    return render(request, 'main/contact.html')


def logout(request):
    return render(request, 'registration/logout.html')


def login(request):
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'registration/register_form.html', args)


def profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html', args)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'registration/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('profile'))
        else:
            return redirect(reverse('change-password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'registration/change-password.html', args)


def event_list(request):
    event = Event.objects.filter(created_date__lte=timezone.now())
    return render(request, 'main/events.html',
                 {'events': event})

