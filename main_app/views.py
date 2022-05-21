from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, FormView
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


class Viewing(FormView):
    model = ViewingRequest
    form_class = ViewingRequestForm
    template_name = 'viewing-request.html'
    success_url = '/'

    # Solution to include the property_id in the form context
    # https://stackoverflow.com/questions/8903601/how-to-process-a-form-via-get-or-post-using-class-based-views
    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['property'] = Properties.objects.get(id=kwargs['propery_id'])
        return self.render_to_response(context)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    