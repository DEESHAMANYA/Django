from django.http import JsonResponse

class basicMiddleware:
    def __init__(self,get_response):
        self.get_response= get_response


    def __call__(self,request):
        # print(request,"hello")
        if(request.path == "/student/"):
            print(request.method,"method")
            print(request.path)
        response=self.get_response(request)
        return response
    
class basicMiddleware1:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/greet/"):
            print(request.method,"Method")
            print(request.path)
        response1=self.get_response(request)
        return response1
    
class basicMiddleware2:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        if(request.path=="/infoo"):
            print(request.method)
            print(request.path)
        response = self.get_response(request)
        return response
    
class basicMiddleware3:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/dyanmaic"):
            print(request.method)
            print(request.path)
        response= self.get_response(request)
        return response
        
    
# class singupMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self, request):   # whenever we make a reqauest
#         data = json.loads(request.body)
#         username=data.get("username")
#         email=data.get("email")
#         dob = data.get("dob")
#         password=data.get("password")
#         # check username rules with regex
#         # check email rules with regex
#         # check dob rules with regex
#         # check password rules with regex

class SscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ['/job1/','/job2/']):
            ssc_results=request.GET.get("SSC",False)
            if(ssc_results !='true'):
                return JsonResponse({"ERROR":"You should qualify ssc for applying this job"},status=400)
            
        return self.get_response(request)


class MedicalfitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=='/job1/'):
            Medical_fit_requaest=request.GET.get("medically_fit",False)
            if(Medical_fit_requaest != 'true'):
                return JsonResponse({"error":"Yu can not medically fit toapply fot=r this job role"},status=400)
        return self.get_response(request)

class AgeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ['/job1/','/job2/']):
            Age_checker=int(request.GET.get("Age",17))
            if(Age_checker>=25 and Age_checker<18):
                return JsonResponse({"error":"Age must be in between 18 and 25" },status=400)
        return self.get_response(request)
