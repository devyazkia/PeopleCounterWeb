from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from django.template.loader import get_template

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

class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["10.00", "11.00", "12.00", "13.00", "14.00", "15.00", "16.00", "17.00", "18.00", "19.00", "20.00", "21.00"]
   
        rows = rekap_pengunjung.objects.filter(tanggal= get)
        data = []
        rowarray_list = []
        for row in rows:
            # t9 = json.dumps((row.pukul09))            
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

# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         template =  get_template('index.html')
#         rows = rekap_pengunjung.objects.filter(tanggal= get)
#         for row in rows:
#             # t9 = json.dumps((row.pukul09))            
#             t10 = json.dumps((row.pukul10))
#             t11 = json.dumps((row.pukul11))
#             t12 = json.dumps((row.pukul12))
#             t13 = json.dumps((row.pukul13))
#             t14 = json.dumps((row.pukul14))
#             t15 = json.dumps((row.pukul15))
#             t16 = json.dumps((row.pukul16))
#             t17 = json.dumps((row.pukul17))
#             t18 = json.dumps((row.pukul18))
#             t19 = json.dumps((row.pukul19))
#             t20 = json.dumps((row.pukul20))
#             t21 = json.dumps((row.pukul21))
#         context = {
#             "rekap_pengunjung.tanggal" : get,
#             "rekap_pengunjung.pukul10" : t10,
#             "rekap_pengunjung.pukul11" : t11,
#             "rekap_pengunjung.pukul12" : t12,
#             "rekap_pengunjung.pukul13" : t13,
#             "rekap_pengunjung.pukul14" : t14,
#             "rekap_pengunjung.pukul15" : t15,
#             "rekap_pengunjung.pukul16" : t16,
#             "rekap_pengunjung.pukul17" : t17,
#             "rekap_pengunjung.pukul18" : t18,
#             "rekap_pengunjung.pukul19" : t19,
#             "rekap_pengunjung.pukul20" : t20,
#             "rekap_pengunjung.pukul21" : t21,
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('index.html', context)
#         return HttpResponse(pdf)

#  from django.http import HttpResponse
#  from django.views.generic import View

#  from yourproject.utils import render_to_pdf #created in step 4

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(), 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('templates/coba.html', data)
        return HttpResponse(pdf, content_type='myproject/template')

