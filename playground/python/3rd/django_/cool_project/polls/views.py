from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    username = "kosciej"
    password = "abc"
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)

    return render(request, "test.html")
    # return HttpResponse("Hello, world. You're at the polls index.")


def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")
