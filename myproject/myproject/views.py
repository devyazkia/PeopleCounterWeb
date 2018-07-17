import csv
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from django.template.loader import get_template
from django.contrib.auth.models import User

from .forms import DataForm
from .model import rekap_pengunjung
import json
import datetime
from .utils import render_to_pdf

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()
now = datetime.datetime.now()
get = now.strftime("%Y-%m-%d")

def index(request):
    status = ''
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = DataForm()
        return render(request, 'index.html', {'form': form, 'datas': rekap_pengunjung.objects.filter(tanggal=  get), 'status': status })  

def history(request):
    status = ''
    form = DataForm()
    return render(request, 'history.html', {'form': form, 'datas': rekap_pengunjung.objects.filter(tanggal= get), 'status': status })  

def export(request):
    status = ''
    form = DataForm()
    return render(request, 'export.html', {'form': form, 'datas': rekap_pengunjung.objects.all(), 'status': status })  
    
class getHistory(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(request, date):
        status = ''
        form = DataForm()
        labels = ["10.00", "11.00", "12.00", "13.00", "14.00", "15.00", "16.00", "17.00", "18.00", "19.00", "20.00", "21.00"]
        rows = rekap_pengunjung.objects.filter(tanggal= '{}'.format(date))
        data = []
        rowarray_list = []
        for row in rows:
            t10 = json.dumps((row.pukul10))
            t11 = json.dumps((row.pukul11))
            t12 = json.dumps((row.pukul12))
            t13 = json.dumps((row.pukul13))
            t14 = json.dumps((row.pukul14))
            t15 = json.dumps((row.pukul15))
            t16 = json.dumps((row.pukul16))
            t17 = json.dumps((row.pukul17))
            t18 = json.dumps((row.pukul18))
            t19 = json.dumps((row.pukul19))
            t20 = json.dumps((row.pukul20))
            t21 = json.dumps((row.pukul21))
        if rows.count() == 0:
            default_item = []
        else:
            default_item = [t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21]
        datajson = {
            "labels" : labels,
            "default" : default_item,
        }
        return Response(datajson)

def getData(request, date):
    status = ''
    form = DataForm()
    return render(request, 'history.html', {'form': form, 'datas': rekap_pengunjung.objects.filter(tanggal= '{}'.format(date)), 'status': status })

def export_history(request, date):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'
        
    writer = csv.writer(response)
    writer.writerow(['Tanggal', 'pukul 10', 'pukul 11', 'pukul 12', 'pukul 13', 'pukul 14', 'pukul 15', 'pukul 16', 'pukul 17', 'pukul 18', 'pukul 19', 'pukul 20', 'pukul 21'])

    users = rekap_pengunjung.objects.filter(tanggal= '{}'.format(date)).values_list('tanggal', 'pukul10', 'pukul11', 'pukul12', 'pukul13', 'pukul14', 'pukul15', 'pukul16', 'pukul17', 'pukul18', 'pukul19', 'pukul20', 'pukul21')
    for user in users:
        writer.writerow(user)

    return response

def export_range(request):
    first_date = datetime.date(2018, 6, 29)
    last_date = datetime.date(2018, 7, 12)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'
        
    writer = csv.writer(response)
    writer.writerow(['Tanggal', 'pukul 10', 'pukul 11', 'pukul 12', 'pukul 13', 'pukul 14', 'pukul 15', 'pukul 16', 'pukul 17', 'pukul 18', 'pukul 19', 'pukul 20', 'pukul 21'])

    users = rekap_pengunjung.objects.filter(tanggal=(first_date, last_date)).values_list('tanggal', 'pukul10', 'pukul11', 'pukul12', 'pukul13', 'pukul14', 'pukul15', 'pukul16', 'pukul17', 'pukul18', 'pukul19', 'pukul20', 'pukul21')
    for user in users:
        writer.writerow(user)

    return response


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["10.00", "11.00", "12.00", "13.00", "14.00", "15.00", "16.00", "17.00", "18.00", "19.00", "20.00", "21.00"]
   
        rows = rekap_pengunjung.objects.filter(tanggal= get)
        data = []
        rowarray_list = []
        for row in rows:
            t10 = json.dumps((row.pukul10))
            t11 = json.dumps((row.pukul11))
            t12 = json.dumps((row.pukul12))
            t13 = json.dumps((row.pukul13))
            t14 = json.dumps((row.pukul14))
            t15 = json.dumps((row.pukul15))
            t16 = json.dumps((row.pukul16))
            t17 = json.dumps((row.pukul17))
            t18 = json.dumps((row.pukul18))
            t19 = json.dumps((row.pukul19))
            t20 = json.dumps((row.pukul20))
            t21 = json.dumps((row.pukul21))
            
        if rows.count() == 0:
            default_item = []
        else:
            default_item = [t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21]
        datajson = {
            "labels" : labels,
            "default" : default_item,
        }
        return Response(datajson)


def export_users_csv(request):
    now = datetime.datetime.now()
    get = now.strftime("%Y-%m-%d")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Tanggal', 'pukul 10', 'pukul 11', 'pukul 12', 'pukul 13', 'pukul 14', 'pukul 15', 'pukul 16', 'pukul 17', 'pukul 18', 'pukul 19', 'pukul 20', 'pukul 21'])

    users = rekap_pengunjung.objects.filter(tanggal= '{}'.format(get)).values_list('tanggal', 'pukul10', 'pukul11', 'pukul12', 'pukul13', 'pukul14', 'pukul15', 'pukul16', 'pukul17', 'pukul18', 'pukul19', 'pukul20', 'pukul21')
    for user in users:
        writer.writerow(user)

    return response


# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'today': datetime.date.today(), 
#             'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('templates/coba.html', data)
#         return HttpResponse(pdf, content_type='myproject/template')

