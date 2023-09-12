from django.db import models
import os

# Create your models here.
class File(models.Model):
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return os.path.basename(self.file_path)
    
    def content(self):
        with open(self.file_path, "r") as f:
            return f.read()
        
    def size(self):
        return os.path.getsize(self.file_path)
