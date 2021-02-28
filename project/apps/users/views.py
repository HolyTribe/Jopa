from django.shortcuts import render
from django.views import generic
from apps.users.forms import LoginForm, PasswordResetForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
#TODO:Сделать ответы жсоном
# После того, как поставят галп
# А еще, я пойму, что ето ваще такое да
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(generic.FormView):
    '''Да ето вьюха для логина а што
    '''
    form_class = LoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data["password"]
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return HttpResponseRedirect(reverse('profile'))
        else:
            return HttpResponseRedirect(reverse('profile'))
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('invalid'))


class Profile(LoginRequiredMixin, generic.View):
    '''Личный кабинет.\n
    Пока что только так, потому что я нз, как ваще все будет
    выглядеть в будущем.\n
    lazy reverse потому что с обычным
    вьюха не дружит, документация рассказывает об этом что-то\n
    Но я не читал, я унгабунга
    '''
    login_url = reverse_lazy('login')
    template_name = 'users/success.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UserChangePassword(generic.FormView):
    '''Смена пароля кароче,
    главное не забыть, что я сделал форму, а дата из поста.
    На самом деле, какая разница,
    правда?)))))))))))))))))))
    '''
    form_class = PasswordResetForm
    success_url = reverse_lazy('profile')
    template_name = 'users/password_change.html'

    # TODO: а нафик я форму делал, а потом беру дату из поста 
    def post(self, request, *args, **kwargs):
        success = True
        old_password = request.POST.get('old_password', None)
        new_password = request.POST.get('password', None)
        new_password_repeat = request.POST.get('password_repeat', None)
        if not new_password == new_password_repeat:
            success = False
            return HttpResponseRedirect(reverse('invalid'))
        user = authenticate(
            email=self.request.user.email,
            password=old_password)
        if user is None:
            success = False
            return HttpResponseRedirect(reverse('invalid'))
        elif success:
            user.set_password(new_password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('profile'))

# TODO: Вот ето дропнуть, как только жсон
class InvalidView(generic.View):
    '''Эта вьюха, чтобы выкидывать ошибку,
    пока я не понял как работает галп
    '''
    template_name = 'users/invalid.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

# Тут точно нужен комментарий?
class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
        