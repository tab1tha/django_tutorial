from django.db import models

# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length=200)
    date_uploaded = models.DateTimeField(db_comment="date and time when file was uploaded")