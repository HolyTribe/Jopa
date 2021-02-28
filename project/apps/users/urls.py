from django.urls import include, path
from apps.users.views import Login, Profile, InvalidView, UserChangePassword, LogoutView
from apps.users.forms import PasswordChangeForm
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
)
from django.urls import reverse_lazy

# TODO:Переопределить стандартные пути для шаблоново ресета, чтобы не хламить мейнтемплейты
app_name = "users"
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('profile/', Profile.as_view(), name='profile'),
    # TODO: ДРОПНУТЬ!!!!!!
    path('invalid/', InvalidView.as_view(), name='invalid'),
    path('profile/password-change',
        UserChangePassword.as_view(),
        name='password-change'),
    path('logout', LogoutView.as_view(), name='logout'),

    # Ресет пароля
    path('password/reset/',
        PasswordResetView.as_view(
            email_template_name='registration/password_reset_email.html', 
            success_url=reverse_lazy('users:password_reset_done')),
            name='password_reset'),
    path("password/change/",
        PasswordChangeView.as_view(
            success_url='/users/password/change/',
            template_name='users/change_password.html'),
        name="password_change"),
    path(
        "password/reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done"),
    path(
        "password/reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            # не могу понять почему эта вещь кидает
            # __init__() got an unexpected keyword argument 'user'
            # form_class=PasswordChangeForm,
            success_url=reverse_lazy('users:password_reset_complete')
            ),
        name="password_reset_confirm"),
    path(
        "password/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete"),    
]
