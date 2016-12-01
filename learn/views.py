from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"I am Maffee !\n from 晓壹科技")


def home(request):
    string = u"我是Maffee，我在学习Django建站~"
    FEList = ["HTML", "CSS", "JavaScript", "jQuery", "AngularJS", "JSON"]
    BEDict = {'name': "Python", 'archi': "Django", "star": "5"}
    return render(request, 'home.html', {'string': string, 'FEList': FEList, 'BEDict': BEDict})
