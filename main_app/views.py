from django.shortcuts import render

def home(request):
    context = {
        'hero_title': 'Find the best properties to rent in the area',
    }
    return render(request, 'index.html', context)
