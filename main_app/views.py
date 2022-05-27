from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from .models import Properties, ViewingRequest
from .forms import ViewingRequestForm


class Home(View):
    def get(self, request):
        context = {
            'hero_title': 'Find the best properties to rent in the area',
        }
        return render(request, 'index.html', context)


class PropertyBrowser(ListView):
    model = Properties
    queryset = model.objects.filter(is_published=True).order_by('-list_date')
    template_name = 'property-browser.html'
    context_object_name = 'properties'
    paginate_by = 3


class Viewing(View):
    template_name = 'viewing-request.html'
    success_message = (
        'We received your request, we will get back to you shortly.')
    permission_denied_message = (
        'You need to log in to your account to book a viewing')
    already_booked_message = (
        'You have previously requested a viewing for this property')

    def get(self, request, property_id, *args, **kwargs):
        user = request.user
        # Check if user is logged in
        if not user.is_authenticated:
            messages.warning(request, self.permission_denied_message)
            return redirect('login')

        # Check if user already booked an appointment for this property
        user_viewings = ViewingRequest.objects.filter(for_user=user)
        _property = Properties.objects.get(id=property_id)
        if user_viewings.filter(property=_property).count() > 0:
            messages.warning(request, self.already_booked_message)
            return redirect('home')

        form = ViewingRequestForm()
        context = {
            'property': _property,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, property_id, *args, **kwargs):
        form = ViewingRequestForm(request.POST)

        # Solution to include the property foreign key in the form
        # https://stackoverflow.com/questions/17126983/add-data-to-modelform-object-before-saving
        if form.is_valid():
            obj = form.save(commit=False)
            obj.property = Properties.objects.get(id=property_id)
            obj.for_user = request.user
            obj.save()

            messages.success(request, self.success_message)
            return redirect('home')
