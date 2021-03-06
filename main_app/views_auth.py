from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm, UserProfileForm


def test_user_logged_in(func):
    '''Redirect request for logged in users with a message'''
    def wrapper(*args, **kwargs):
        request = args[0].request
        if request.user.is_authenticated:
            messages.warning(request, 'You are already logged in.')
            return redirect('home')
        return func(*args, **kwargs)
    return wrapper


class Login(SuccessMessageMixin, LoginView):
    success_message = 'You are logged in'
    extra_context = {
        'page_title': 'Login',
    }

    @test_user_logged_in
    def get(self, request, *args, **kwargs):
        self.extra_context.update({'active': request.resolver_match.view_name})
        return super().get(request, *args, **kwargs)

    @test_user_logged_in
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class Logout(SuccessMessageMixin, LogoutView):
    success_message = 'You are logged out'


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
            'page_title': 'Register',
            'active': request.resolver_match.view_name,
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
            return redirect('login')
        else:
            context = {
                'register_form': r_form,
                'profile_form': p_form,
            }
            return render(request, self.template_name, context)
