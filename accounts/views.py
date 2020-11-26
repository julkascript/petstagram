from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from accounts.forms import SignupForm
from accounts.models import UserProfile


def user_profile(request, pk=None):
    context = {

    }
    return render(request, 'accounts/user_profile.html', context)


def signup_user(request):
    if request.method == 'GET':
        context = {
            'form': SignupForm(),
        }
        return render(request, 'accounts/signup.html', context)
    form = SignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        profile = UserProfile(
            user=user,
        )
        profile.save()
        login(request, user)
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def signout_user(request):
    logout(request)
    return redirect('index')