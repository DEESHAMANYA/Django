from django.shortcuts import render
from django.http import HttpResponse
# from django.http import JsonResponse


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
# def sample(request):
#     return HttpResponse('Hello World')

# def sample1(request):
#     return HttpResponse('Welcome to Django')

# def sampleInfo(request):
#     data = {"name":'sumanth'}
#     return JsonResponse(data)

# def dynamicResponse(request):
#     name = request.GET.get("name",'')
#     # data = request.Get.get("name":"suman","city":"hyd")
#     return HttpResponse(f"hello {name}")



