from django.contrib.auth import login, authenticate
# TODO:Сделать ответы жсоном
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import JsonResponse
from apps.users.forms import LoginForm, PasswordChangeForm
from apps.users.models import User


class Login(generic.FormView):
    """Обработчик логина"""
    form_class = LoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return JsonResponse({'errors':False, 'redirect':'http://127.0.0.1:8000/account/profile/5'})
        else:
            return JsonResponse({'errors':True, 'message':'Учетная запись не валидна'})

    def form_invalid(self, form):
        return JsonResponse({'errors':True, 'fields':form.errors, 'message':"Проверьте указанные поля"})


class ProfileDetailView(generic.DetailView):
    """Личный кабинет"""
    template_name = 'users/profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object().profile.first()
        return context


class UserChangePassword(generic.FormView):
    """Смена пароля, если юзер авторизован"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/password_change.html'

    def form_valid(self, form):
        # success - заготовка для жсонреспонсов
        success = True
        old_password = form.cleaned_data['old_password']
        new_password = form.cleaned_data['password']
        new_password_repeat = form.cleaned_data['password_repeat']
        if not new_password == new_password_repeat:
            success = False
            return JsonResponse({'errors':True, 'fields':form.errors})
        user = authenticate(
            username=self.request.user.username,
            password=old_password)
        if user is None:
            success = False
            return JsonResponse({'errors':True, 'fields':"Что-то пошло не так, пользователя не существует!"})
        elif success:
            user.set_password(new_password)
            user.save()
            login(self.request, user)
            return HttpResponseRedirect(reverse('users:profile'))

    def form_invalid(self, form):
        return JsonResponse({'errors': True, 'fields':form.errors})
