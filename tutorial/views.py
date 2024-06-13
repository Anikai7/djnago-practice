from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"form.html")

def details(request):
    mydictonary={
        "mail" : request.POST["exampleFormControlInput1"],
        "message": request.POST['exampleFormControlTextarea1'],
        "method": request.method
    }
    return JsonResponse( mydictonary)


