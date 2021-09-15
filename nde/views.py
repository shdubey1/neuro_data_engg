from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

# import local data
from .serializers import GeeksSerializer, HeroSerializer
from .models import GeeksModel
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

#create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = GeeksModel.objects.all()
    #queryset.save()
	# specify serializer to be used
	serializer_class = GeeksSerializer

#@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def userapi(request):
    tutorial_data = JSONParser().parse(request)
    #print(request.body)
    tutorial_serializer = HeroSerializer(data=tutorial_data)
    if tutorial_serializer.is_valid():
        return JsonResponse(tutorial_serializer.data)
    return HttpResponse("all ok")




# Create your views here.
# @api_view(['GET','POST'])
@csrf_exempt
def viewset(request):
    print("hello12")
    queryset = GeeksModel.objects.all()
    print(request.headers)
    data_serial = GeeksSerializer(queryset,many=True) 
    return JsonResponse(data_serial.data, safe=False)


def index(request):
    return render(request,'nde/dashboard.html')

def dataset(request):
    print(request)
    return render(request,'nde/dataset.html')

def test(request):
    print('EDA Button clicked')

    return render(request,'nde/test.html')

def previewDataset(request):
    dataframe = pd.read_csv('G:\internship_project\dataset\data.csv') 
    dataframe_html = dataframe.to_html()
    return HttpResponse(dataframe_html)#render(request,'nde/dataset.html',param)    
