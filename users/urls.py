from django.urls import path
from users.views import UserRegisterView, UserEditView, ProfilePageView, EditProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('<int:pk>/profile', ProfilePageView.as_view(), name='show_profile'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
]