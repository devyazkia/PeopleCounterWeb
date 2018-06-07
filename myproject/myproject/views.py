from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from .forms import DataForm
from .model import jml_pelanggan
import json
import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()
now = datetime.datetime.now()
get = now.strftime("%Y-%m-%d")
# get = '2018-04-02'

def index(request):
    status = ''
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = DataForm()
        return render(request, 'chart.html', {'form': form, 'datas': jml_pelanggan.objects.filter(tanggal=  get), 'status': status })  

def history(request):
    status = ''
    form = DataForm()
    return render(request, 'charthistory.html', {'form': form, 'datas': jml_pelanggan.objects.filter(tanggal=  get), 'status': status })  

class GenreListView(ListView):
    model = jml_pelanggan
    template_name = 'index.html'
    def get_queryset(request, pk):
        datax = jml_pelanggan.objects.filter(tanggal= get)
        if query:
           return datax.filter(date=query)
        return datax

class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["10.00", "11.00", "12.00", "13.00", "14.00", "15.00", "16.00", "17.00", "18.00", "19.00", "20.00", "21.00"]
   
        rows = jml_pelanggan.objects.filter(tanggal= get)
        data = []
        rowarray_list = []
        for row in rows:
            t9 = json.dumps((row.pukul09))            
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
            # j = json.dumps(t9)
            # jj = json.dumps(tt)
            # data.append(j)
        default_item = [ t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20]
        datajson = {
            "labels" : labels,
            "default" : default_item,
        }
        return Response(datajson)
