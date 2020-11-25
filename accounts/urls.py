from django.urls import path

from accounts.views import profile_display, sign_up

urlpatterns = [
    path('profile/<int:pk>', profile_display, name="user profile"),
    path('signup/', sign_up, name="sign up")
]
