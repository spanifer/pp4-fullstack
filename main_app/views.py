import imp
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Properties

def home(request):
    context = {
        'hero_title': 'Find the best properties to rent in the area',
    }
    return render(request, 'index.html', context)


class PropertyBrowser(View):

    def get(self, request, *args, **kwargs):
        properties = Properties.objects.filter(is_published=True)
        context = {
            'properties': properties,
        }
        return render(request, 'property-browser.html', context=context)
