from django.shortcuts import render, HttpResponse

def index(request):
    print(request)
    return HttpResponse("Hello, world. You're at the polls app index.")

