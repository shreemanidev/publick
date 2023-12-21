from django.shortcuts import render, redirect
from .models import * 

def homePage(request):
    if request.method == "POST":
        e = Contact()
        e.name = request.POST.get("name")
        e.email = request.POST.get("email")
        e.subject = request.POST.get("subject")
        e.message = request.POST.get("message")
        e.save()
        return redirect("/")
    return render(request, "index.html")


def join(Request):    
    if(Request.method=="POST"):
       j = Join()
       j.name = Request.POST.get("name")
       j.email = Request.POST.get("email")
       j.contact = Request.POST.get("contact")
       j.pan = Request.FILES.get("pan")
       j.aadhar= Request.FILES.get("aadhar")
       j.photo= Request.FILES.get("photo")
       j.certificate= Request.FILES.get("certificate")
       j.save()
    return redirect("/")
