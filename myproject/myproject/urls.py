from django.contrib import admin
from django.urls import path

from rest_framework import routers
from . import views
# from myproject.views import get_data
from .views import ChartData

urlpatterns = [
    path('api/chart/data/', ChartData.as_view()),
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),    
    # path(r'^generate_pdf/$', "analytics.views.GroupPDFGenerate.as_view()", name="generate_pdf"),
    path('admin/', admin.site.urls),
    path(r'^posts/(?P<slug>[-\w]+)/$', views.index, name='index'),
    # path(r'^$', views.index, name="index"), 
]
