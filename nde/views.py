from django.db import models
from nde.EDA.MissingValuesFuncs import MissingValuesFuncs
from nde.EDA.EDAFuncs import EDAFuncs
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

# import local data
from .serializers import EDAJSONSerializer, GeeksSerializer, HeroSerializer
from .models import EDA, EDAJSON, GeeksModel, MissingValues
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import io


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

@csrf_exempt
def csvfile(request):
    # print(request.body)
    # print(type(request.body))
    #df = pd.DataFrame(request.body, ).to_csv()
    urlData = request.body
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    eda = EDAFuncs(df, request)
    #a = eda.missingValuesHtml().content
    eda_json = EDAJSON(graphs=eda.graphHtml(),

    missing_vals=eda.missingValuesHtml().content,
    correlation = eda.correlationHtml(),
    missing_vals_plotting=eda.missingValuesPlottingHtml(),
    sample_of_first_n_last_rows=eda.sampleOfFstnLstRowHtml())

    #j_data = JSONParser.parse(eda_json)
    #eda_json_ser = EDAJSONSerializer(data = j_data)
    #if eda_json_ser.is_valid():
    #   return JsonResponse(eda_json_ser.data)
    #edaJSON = {'Missing Values' : 'eda.missingValuesHtml().content'}
    
    #print('Shubham',a.content)
    # missing_values = df.isnull().sum()
    # missing_values_sum=0
    # for i in missing_values:
    #     if i !=0:
    #         missing_values_sum+=i
    #print(missing_values_sum)
    #queryset = GeeksModel.objects.all()
    #print(request.headers)
    data_serial = EDAJSONSerializer(eda_json,many=False) 
    return JsonResponse(data_serial.data, safe=False)
    #return HttpResponse(edaJSON)




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
