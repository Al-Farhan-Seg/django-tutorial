from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def al_farhan(request):
    return HttpResponse("Farhan has tried it out very well!!!")