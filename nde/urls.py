from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'ndeapi', GeeksViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Ndehome"),
    path('test/', views.test),
    path('api/viewset',views.viewset),
    path('dataset',views.dataset),
    path('previewDataset/', views.previewDataset, name="Ndehome"),
    path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls')),
    path('button/', views.test, name="test"),
    path('user/',views.userapi)

]
