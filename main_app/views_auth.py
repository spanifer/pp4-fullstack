from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm, LoginForm


def test_user_logged_in(func):
    '''Redirect request for logged in users with a message'''
    def wrapper(*args, **kwargs):
        request = args[0].request
        if request.user.is_authenticated:
            messages.warning(request, 'You are already logged in.')
            return redirect(reverse('home'))
        return func(*args, **kwargs)
    return wrapper


class Login(LoginView):
    form_class = LoginForm

    @test_user_logged_in
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @test_user_logged_in
    def post(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class Register(View):

    success_message = 'You have successfully registered'
    template_name = 'registration/register.html'

    @test_user_logged_in
    def get(self, request):
        r_form = UserRegisterForm()
        p_form = UserProfileForm()
        context = {
            'register_form': r_form,
            'profile_form': p_form,
        }
        return render(request, self.template_name, context)

    @test_user_logged_in
    def post(self, request):
        r_form = UserRegisterForm(request.POST)
        p_form = UserProfileForm(request.POST)
        if r_form.is_valid() and p_form.is_valid():
            r_form.save()
            obj = p_form.save(commit=False)
            obj.user = r_form.instance
            obj.save()
            messages.success(request, self.success_message)
            return redirect(reverse('login'))
        else:
            context = {
                'register_form': r_form,
                'profile_form': p_form,
            }
            return render(request, self.template_name, context)
