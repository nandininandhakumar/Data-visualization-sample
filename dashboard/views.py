
from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from dashboard.models import *

def home(request):
    return render(request, 'home.html')

def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
   
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def datatable_static(request):
    labels = []
    data = []
    
    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
 
    datas = zip(labels,data)
    return render(request, 'datatable/datatable_static.html', {'data': datas})
        