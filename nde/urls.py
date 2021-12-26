from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import *

# define the router
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Ndehome"),
    path('test/', views.test),
    path('dataset',views.dataset),
    path('previewDataset/', views.previewDataset, name="Ndehome"),
    path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls')),
    path('button/', views.test, name="test"),
    path('csvfile/',views.csvfile),
    path('missing_values_api/',views.missingValuesAPI),
    path('correlation_api/',views.correlationAPI),
    path('missing_values_plotting_api/',views.missingValuesPlottingAPI),
    path('sample_of_first_n_last_rows_api/',views.sampleOfFirstNLastRowsAPI),
    path('graphs_api/',views.graphsAPI),


    path('up_sampling_api/',views.upSamplingAPI)


]
