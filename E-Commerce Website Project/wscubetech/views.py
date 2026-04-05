from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data={
        "title":"Home New",
        'clist':["java,","c++","Django","python","MySQL"],
        "student":[
            {'name':'Manish Verma','phone':9125697807},
            {'name':'Suhani Singh','phone':9519441328}
        ]
    }
    return render(request,"index.html",data)

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def courseDetail(request,courseid):
    return HttpResponse(courseid)