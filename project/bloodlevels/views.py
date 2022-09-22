from django.shortcuts import render
from .models import Date, Level


# homepage view
def home_view(request):
    queryset_dates = Date.objects.all()
    queryset_levels = Level.objects.all()

    context = {
        'dates': queryset_dates,
        'levels': queryset_levels,
    }

    return render(request, 'home.html', context)