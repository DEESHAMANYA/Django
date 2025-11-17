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
    print(request.method)
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

        
    elif request.method=="GET":
        result = list(Student.objects.values()) # get all records 
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200) #"returns all records "


        # get specific record by ref_id
        # data=json.loads(request.body)
        # ref_id=data.get("id")
        # stud_id=list(Student.objects.filter(id=ref_id).values())
        # return JsonResponse({"status":"sucess","filtered_data":stud_id},status=200)

        # filter age >=20 and age<=25
        # "__gte and __lte"

        # using dyanmic value
        # age_gre=data.get("age")
        # student_age=list(Student.objects.filter(age__gte=age_gre).values())

        # student_age=list(Student.objects.filter(age__lte=20).values())
        # student_age=list(Student.objects.filter(age__lte=20).values())
        # return JsonResponse({"status":"ok","data":student_age},status=200)
    
        # order by name
        # "-name --- desecnding order"
        # student_name=list(Student.objects.order_by('-name').values())
        # return JsonResponse({"status":"ok","data":student_name},status=200)

    elif request.method=="PUT":
        data=json.loads(request.body)
        ref_id=data.get("id")
        new_email=data.get("email")
        existing_student=Student.objects.get(id=ref_id) # fetched the object as per the id
        existing_student.email=new_email #updating with new email
        existing_student.save()

        updated_data=Student.objects.filter(id=ref_id).values().first()
        print(updated_data)
        # return JsonResponse({"req":"PUT method requested"},status=200)
        return JsonResponse({"statsu":"data updated successfully","data":updated_data},status=200)
    


    elif request.method =="DELETE":
        data = json.loads(request.body)
        ref_id=data.get("id")
        getting_deleted_data=Student.objects.filter(id=ref_id).values().first()

        to_be_delete=Student.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"status":"success","message":"student record deleted sucessfully","deleted data":getting_deleted_data},status=200)
    return JsonResponse({"error":"use POST method"},status=400)


def job1(request):
    return JsonResponse({"Message":"You have SUCCESSFULLY applied for job1"},status=200)
def job2(request):
    return JsonResponse({"Message":"You have SUCCESSFULLY applied for job2"},status=200)
