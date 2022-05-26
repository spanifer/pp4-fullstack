from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .models import Properties
from .forms import ViewingRequestForm, UserRegisterForm, UserProfileForm, LoginForm

class Home(View):
    def get(self, request):
        context = {
            'hero_title': 'Find the best properties to rent in the area',
        }
        return render(request, 'index.html', context)


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class Register(View):

    success_message = 'You have successfully registered'

    def get(self, request):
        r_form = UserRegisterForm()
        p_form = UserProfileForm()
        context = {
            'register_form': r_form,
            'profile_form': p_form,
        }
        return render(request, 'register.html', context)

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
            return render(request, 'register.html', context)


class PropertyBrowser(ListView):
    model = Properties
    queryset = model.objects.filter(is_published=True).order_by('-list_date')
    template_name = 'property-browser.html'
    context_object_name = 'properties'
    paginate_by = 3


class Viewing(View):
    success_url = '/'
    template_name = 'viewing-request.html'

    def get(self, request, propery_id, *args, **kwargs):
        form = ViewingRequestForm()
        property = Properties.objects.get(id=propery_id)
        context = {
            'property': property,
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request, propery_id, *args, **kwargs):
        form = ViewingRequestForm(request.POST)

        # Solution to include the property foreign key in the form
        # https://stackoverflow.com/questions/17126983/add-data-to-modelform-object-before-saving
        if form.is_valid():
            obj = form.save(commit=False)
            obj.property = Properties.objects.get(id=propery_id)
            obj.save()
            return render(request, self.success_url)
