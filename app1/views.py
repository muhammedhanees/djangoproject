from django_project.settings import TEMPLATES
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfun(request):
    # print('heloooooo')
    return HttpResponse('helooo baabte')


def samplefun(request):
    return render(request,'template.html')

    
