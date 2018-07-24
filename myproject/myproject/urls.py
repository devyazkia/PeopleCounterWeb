from django.contrib import admin
from django.urls import path

from rest_framework import routers
from . import views
# from myproject.views import ,get_data
from .views import ChartData, getData

urlpatterns = [
    path('api/chart/data/', ChartData.as_view()),
    # path('api/chart/datahistory/', getHistory.as_view()),
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('export/', views.export, name='export'), 
    path('export/dateFrom=<dateFrom>&dateTo=<dateTo>', views.exportResults, name='export'),   
    path('^export/csv/$', views.export_users_csv, name='export_users_csv'),  
    path('admin/', admin.site.urls),
    path('history/date=<date>', views.getData),
    path('exporthistory/csv/$', views.export_history, name='export_history'),  
    path('exportrange/csv/$', views.export_range, name='export_range'),      
    # path('history/date=<date>', views.getData),
    # path('^posts/(?P<slug>[-\w]+)/$', views.getHistory),
    # path(r'^$', views.index, name="index"), 
]
