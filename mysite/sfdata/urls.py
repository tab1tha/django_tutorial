from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api", views.api, name="api"),
    path("api/files/upload", views.upload, name="upload"),
    path("api/files/download", views.download, name="download"),
    path("api/files", views.files, name="files"),    
]