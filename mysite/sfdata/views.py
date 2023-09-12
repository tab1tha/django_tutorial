from django.http import HttpResponse
from django.shortcuts import render

from .models import File

# Create your views here.
def index(request):
    files = File.objects.all()
    return render(request, "sfdata/index.html", {"file_list": files})
def api(request):
    return HttpResponse("available api endpoints")
def files(request):
    # get files in this directory and list them out
    return HttpResponse("a list of files")
def upload(request):
    return HttpResponse("upload a file")
def download(request, file_id):
    return HttpResponse("download file %s" % file_id)
def view(request, file_id):
    file = File.objects.get(pk=file_id)
    return render(request, "sfdata/view_file.html", {"file": file})
def search(request, file_id):
    return HttpResponse("searching for %s file" % file_id)
def validate(request, file_id=None):
    if file_id:
        return HttpResponse("validation results for %s" %file_id) 
    return HttpResponse("validating file")