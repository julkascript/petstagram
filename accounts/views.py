from django.shortcuts import render


def profile_display(request):
    context = {

    }
    return render(request, 'user_profile.html', context)


def sign_up(request):
    return render(request, 'signup.html')
