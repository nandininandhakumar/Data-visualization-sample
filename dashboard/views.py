
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
    print(queryset[0].population)
    # for entry in queryset:
    #     labels.append(entry['country__name'])
    #     data.append(entry['country_population'])
    # data1 = {}
    # data1['data'] = data
    # data1['labels'] = labels
    # data1 = dict(zip(labels,data))
    # print("COUNTRY, POPULATION")
    # for key, value in data1.items():
    #     labels , data = value
    #     print(labels, data)

    
    # for key,values in data1.items():
    #     for v in values:
    #         print(key, ":" , v)

    # context = {'out': data1.items()}
    # print(context)
    return render(request, 'datatable/datatable_static.html')
    # return render (request,"datatable/datatable_static.html",data1)
        