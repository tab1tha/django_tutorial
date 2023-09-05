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
def download(request, file_id):
    return HttpResponse("download file %s" % file_id)
def search(request, file_id):
    return HttpResponse("searching for %s file" % file_id)
def validate(request, file_id=None):
    if file_id:
        return HttpResponse("validation results for %s" %file_id) 
    return HttpResponse("validating file")