from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
)
from django.urls import path
from django.urls import reverse_lazy

from apps.users.views import Login, ProfileDetailView, InvalidView, UserChangePassword

app_name = "users"
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('profile/<pk>/', ProfileDetailView.as_view(), name='profile'),
    # TODO: ДРОПНУТЬ!!!!!!
    path('invalid/', InvalidView.as_view(), name='invalid'),
    path('profile/password-change/',
         UserChangePassword.as_view(),
         name='password-change'),
    path('logout', LogoutView.as_view(
        template_name='registration/logout.html'
    ), name='logout'),
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
            # form_class=PasswordResetForm,
            # Все еще не смог понять, в чем дело, оставил пока что просто шаблон
            template_name='registration/password_reset_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete')
        ),
        name="password_reset_confirm"),
    path(
        "password/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete"
    ),
]
