from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is index function.</h1>")

def about(request):
    return HttpResponse("This is about function.")    