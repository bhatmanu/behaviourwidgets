from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .modules import widgetmain
import json,os

def index(request):
    return JsonResponse(widgetmain.get_all_nodes(),safe=False)

def create(request):
    content = json.loads(request.body.decode('utf-8'))
    print(content.get('name'))
    print(content.get('appliesTo'))
    print(content.get('process'))
    widgetmain.create(content.get('name'),content.get('appliesTo'),content.get('process'))
    return None

def apply(request):
    content = json.loads(request.body.decode('utf-8'))
    filename = 'widget'+content.get('widget')+'wid.py'
    modulename = 'widget'+content.get('widget')+'wid'
    print(filename)
    print(content.get('nodeid'))
    widgetmain.widget_process(filename,content.get('nodeid'),modulename)
