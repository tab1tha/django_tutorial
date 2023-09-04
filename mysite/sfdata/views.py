from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("welcome to sfdata")
def api(request):
    return HttpResponse("available api endpoints")
def files(request):
    return HttpResponse("a list of files")
def upload(request):
    return HttpResponse("upload a file")
def download(request):
    return HttpResponse("download a file")
