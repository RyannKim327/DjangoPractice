import hashlib

from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def hash(text):
    return (hashlib.sha256(text.encode())).hexdigest()


# Create your views here.


def a(request, id):
    # print(id)
    # return HttpResponse(f"<h3>Hello {id}</h3>")
    data = {"id": id}
    return render(request, "index.html", {"data": data})


def loginForm(request):
    if request.COOKIES["username"] != "":
        return HttpResponse("Logged in")
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = hash(request.POST.get("password", ""))
        user.objects.create(username=username, password=password).save()
        return HttpResponse(f"{username} {password}")
    else:
        return render(request, "registration.html")


def login(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username", "")
            password = hash(request.POST.get("password", ""))
            d = user.objects.get(username__exact=username)
            if password == d.password:
                # return render(request, "index.html", { "data": {
                # 	"msg": "Wrong username or password"
                # }})
                res = HttpResponse(f"Logged in")
                res.set_cookie("username", username)
                return res
            else:
                return render(
                    request,
                    "index.html",
                    {"data": {"msg": "Wrong username or password"}},
                )
        except:
            return render(
                request, "index.html", {"data": {"msg": "Wrong username or password"}}
            )
    try:
        if request.COOKIES["username"] != "":
            return HttpResponse("Logged In")
    except:
        pass
    return render(request, "index.html", {"data": {"msg": "Welcome user"}})
