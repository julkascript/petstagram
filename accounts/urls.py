from django.urls import path

from accounts.views import user_profile, signup_user

urlpatterns = [
    path('profile/<int:pk>/', user_profile, name="user profile"),
    path('signup/', signup_user, name="signup user")
]
