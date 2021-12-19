from django.db import models
from nde.EDA.MissingValuesFuncs import MissingValuesFuncs
from nde.EDA.EDAFuncs import EDAFuncs
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from .serializers import EDAJSONSerializer
from .models import EDA, EDAJSON, MissingValues
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import io

@csrf_exempt
def missingValuesAPI(request):
    urlData = request.body
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    eda = EDAFuncs(df, request)
    missing_vals_html=eda.missingValuesHtml().content
    return HttpResponse(missing_vals_html)

@csrf_exempt
def correlationAPI(request):
    urlData = request.body
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    eda = EDAFuncs(df, request)
    correlation_html = eda.correlationHtml()
    return JsonResponse(correlation_html, safe=False)

@csrf_exempt
def missingValuesPlottingAPI(request):
    urlData = request.body
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    eda = EDAFuncs(df, request)
    missing_values_plotting_html = eda.missingValuesPlottingHtml()
    return JsonResponse(missing_values_plotting_html, safe=False)

@csrf_exempt
def sampleOfFirstNLastRowsAPI(request):
    urlData = request.body
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    eda = EDAFuncs(df, request)
    sample_of_first_n_last_rows_html = eda.sampleOfFstnLstRowHtml()
    return HttpResponse(sample_of_first_n_last_rows_html)

@csrf_exempt
def graphsAPI(request):
    urlData = request.body
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    eda = EDAFuncs(df, request)
    graphs_html = eda.graphHtml()
    return JsonResponse(graphs_html, safe=False)

@csrf_exempt
def csvfile(request):
    urlData = request.body
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    eda = EDAFuncs(df, request)
    eda_json = EDAJSON(graphs=eda.graphHtml(),

    missing_vals=eda.missingValuesHtml().content,
    correlation = eda.correlationHtml(),
    missing_vals_plotting=eda.missingValuesPlottingHtml(),
    sample_of_first_n_last_rows=eda.sampleOfFstnLstRowHtml())
    data_serial = EDAJSONSerializer(eda_json,many=False) 
    return JsonResponse(data_serial.data, safe=False)
    

def index(request):
    return render(request,'nde/dashboard.html')

def dataset(request):
    #print(request)
    return render(request,'nde/dataset.html')

def test(request):
    print('EDA Button clicked')

    return render(request,'nde/test.html')

def previewDataset(request):
    dataframe = pd.read_csv('G:\internship_project\dataset\data.csv') 
    dataframe_html = dataframe.to_html()
    return HttpResponse(dataframe_html)
