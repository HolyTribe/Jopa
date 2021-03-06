from django.contrib.auth import login, authenticate
# TODO:Сделать ответы жсоном
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from apps.users.forms import LoginForm, PasswordChangeForm


class Login(generic.FormView):
    """Да ето вьюха для логина а што
    """
    form_class = LoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            return HttpResponseRedirect(reverse('users:invalid'))

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('users:invalid'))


class Profile(LoginRequiredMixin, generic.View):
    """Личный кабинет"""
    login_url = reverse_lazy('users:login')
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UserChangePassword(generic.FormView):
    """Смена пароля,
    главное не забыть, что я сделал форму, а дата из поста.
    """
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/password_change.html'

    def form_valid(self, form):
        # success - заготовка для жсонреспонсов
        success = True
        old_password = form.cleaned_data['old_password']
        new_password = form.cleaned_data['password']
        new_password_repeat = form.cleaned_data['password_repeat']
        if not new_password == new_password_repeat:
            success = False
            return HttpResponseRedirect(reverse('users:invalid'))
        user = authenticate(
            username=self.request.user.username,
            password=old_password)
        if user is None:
            success = False
            return HttpResponseRedirect(reverse('users:invalid'))
        elif success:
            user.set_password(new_password)
            user.save()
            login(self.request, user)
            return HttpResponseRedirect(reverse('users:profile'))


# TODO: Дропнуть, после жсонреспонсов
class InvalidView(generic.View):
    """Эта вьюха, чтобы выкидывать ошибку,
    пока я не понял как работает галп
    """
    template_name = 'users/invalid.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
