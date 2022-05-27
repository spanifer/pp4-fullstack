from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Properties
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
    success_url = '/'
    template_name = 'viewing-request.html'

    def get(self, request, property_id, *args, **kwargs):
        form = ViewingRequestForm()
        _property = Properties.objects.get(id=property_id)
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
            obj.save()
            return render(request, self.success_url)
