from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. eb698350 is the polls index.")


def hello(request):
    return HttpResponse("Hello, world!")