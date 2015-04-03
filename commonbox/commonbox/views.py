from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.db.models import Q
from commonbox.models import *
import os
import sys
from gcharts import gviz_api
from django.db import connection
import json
from chartit import *
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import datetime
from django.db.models import Sum

def home(request):
    return render(request, 'login.html')

def demo(request):
    return render(request, 'ddd.html')

def clientlogin(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('usrnme', ''):
            errors.append('Enter Username')

        if not request.POST.get('paswrd', ''):
            errors.append('Enter Password')
            
        user = authenticate(username=request.POST.get('usrnme'), password=request.POST.get('paswrd'))
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect('search')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render(request, 'login.html',{'state':state, 'username': request.POST.get('usrnme')})

@login_required
def search(request):
    show_chart = False
    return render_to_response('search_page.html', {'showchart' : show_chart})

def search_result(request):
    '''description = {"detectedapp": ("number", "detected apps"),
                 "month": ("number", "Month"),
                   "manualscan": ("number", "outdated apps"),
                   "outdatedapp": ("number", "vulnerable apps"),
                   "1": ("number", "percent")}
    '''

    description = {"month": ("number", "Month"),"WSS_12": ("number", "WSS_12"),"WSS_13": ("number", "WSS_13")}
    #data = TelemetryHrm.objects.all().values('total_detected_apps', 'month', 'total_outdated_apps',
    #                                         'total_vulnerable_apps')

    data = TelemetryHrm.objects.raw('SELECT * FROM commonbox_telemetryhrm')

    cursor = connection.cursor()
    cursor10 = connection.cursor()
    cursor11 = connection.cursor()

    results = []
    results10 = []

    cursor.execute('SELECT month,total_count FROM commonbox_harshil10 where counter_name="WSS_12" GROUP BY month')
    cursor10.execute('SELECT total_count FROM commonbox_harshil10 where counter_name="WSS_13" GROUP BY month')
    #cursor11.execute('SELECT SUM(counter_value*machine_count) FROM commonbox_harshil10 where counter_name="detectedapp" GROUP BY month')

    row = cursor.fetchall()
    row10 = cursor10.fetchall()
    #row11 = cursor11.fetchall()

    print row
    print row10

    c = zip(*row)+ zip(*row10) #+ zip(*row11)
    res = list(set(zip(*c)))

    cols = ['month', 'WSS_12', 'WSS_13']

    for r in res:
        results.append(dict(zip(cols, r)))

    print results
    
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(results)
    jscode = data_table.ToJSon(columns_order=("month", "WSS_12", "WSS_13"))
    
    #print request.GET.values()

    if request.GET.get('product') == 'VUL':
        print jscode
        return HttpResponse(jscode, content_type='application/json; charset=utf-8')
    else:
        print 'none returned'
        return render_to_response('divdemo.html')








    
    
