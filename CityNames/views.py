from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from urllib.request import urlopen
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def CitySearch(request):
    try:
        import json
        url="https://samples.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=b6907d289e10d714a6e88b30761fae22"
        response=urlopen(url)
        data_json=json.loads(response.read())
        names = list()
        for key,data in data_json.items():
            if(type(data) == list):
                for data2 in data:
                    for key3,data3 in data2.items():
                        if(key3=='name'):
                            names.append(data3)
        countt=[]
        if(str(request.POST.get('namess')).isalpha() == True  ):
            for n in names:
                if(str(request.POST.get('namess')).capitalize() == n[0]):
                    countt.append(n)
            CityCount=len(countt)
            context={'name':countt,'count':str(CityCount)}
        else:
            context={'name':"Please enter valid letter", 'count':"NA"}
        return render(request,'main.html',context)
    except Exception as e:
        print(e)