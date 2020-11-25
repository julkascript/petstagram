from django.shortcuts import render, redirect

from accounts.forms import SignupForm


def user_profile(request, pk):
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
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
