from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication import forms


class RegisterUser(CreateView):
    form_class = forms.RegistrationUserForm
    template_name = 'auth/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'auth/login.html'



def logout_user(request):
    logout(request)
    return redirect('home')
