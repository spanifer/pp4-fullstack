import imp
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Properties

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