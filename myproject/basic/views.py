from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import Student



def add(request):
    a=request.GET.get('a')
    b=request.GET.get('b')

    a= float(a)
    b= float(b)
    result = a+b
    return HttpResponse(result)

def sub(request):
    a=request.GET.get('a')
    b=request.GET.get('b')

    a= float(a)
    b= float(b)
    result = a - b
    return HttpResponse(result)
def mul(request):
    a = request.GET.get('a')
    b = request.GET.get('b')

    a = float(a)
    b = float(b)
    result = a * b
    return HttpResponse(result)


def div(request):
    a = request.GET.get('a')
    b = request.GET.get('b')

    a = float(a)
    b = float(b)
    result = a / b  # Note: will error if b=0
    return HttpResponse(result)

# Create your views here.
def sample(request):
    return HttpResponse('Hello World')

def sample1(request):
    return HttpResponse('Welcome to Django')

def sampleInfo(request):
    data = {"name":'sumanth'}
    return JsonResponse(data)


def dynamicResponse(request):
    name = request.GET.get("name",'')
    # data = request.Get.get("name":"suman","city":"hyd")
    return HttpResponse(f"hello {name}")



# to test te database connection

def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})


@csrf_exempt
def addStudent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        stud=Student.objects.create(
            name=data.get('name'),
            age=data.get('age'),
            email=data.get('email')
            )
        # print(data)
        # data.get('name')
        # data.get('age')
        return JsonResponse({"status":"success","id":stud.id},status=200)
        # return JsonResponse(data)
    return JsonResponse({"error":"use POST method"},status=400)
