from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    marcgis_index = u'MArcGIS 首页'
    return render(request, 'index.html', {'marcgis_index': marcgis_index})


def demo(request):
    demoname = u"SoshineScene - Maffee's GIS 欢迎使用！"
    return render(request, 'demo.html', {'demoname': demoname})


def alpha(request):
    alphaname = u"SoshineSee Alpha"
    return render(request, 'alpha.html', {'alphaname': alphaname})


def alpha_blockdata(request):
    alpha_blockdata = u"SoshineSee BlockData"
    return render(request, 'alpha_blockdata.html', {'alpha_blockdata': alpha_blockdata})


def alpha_radius(request):
    alpha_radius = u"SoshineSee alpha_radius"
    return render(request, 'alpha_radius.html', {'alpha_radius': alpha_radius})
