from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", views.api, name="api"),
    # upload
    path("api/files/upload/", views.upload, name="upload"),
    # download, delete, view
    path("api/files/<int:file_id>/", views.view, name="view_file"),
    # display list of files
    path("api/files/", views.files, name="files"),  
    # search files
    path("api/files/search?<int:file_id>/", views.search, name="search"),
    # validate
    path("api/files/validate/", views.validate, name="validate"),
]
