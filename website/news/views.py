from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Here gonna be news</h1>")