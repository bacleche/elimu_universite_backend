from django.db import models

from user_account.models import Teacher

# Create your models here.
class Folder(models.Model):
    
    label = models.CharField(max_length=20)
    
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Dossier : {self.label} crée par {self.owner}"


class File(models.Model):
    
    label = models.CharField(max_length=20)
    
    inFolder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    
    attachement = models.FileField(upload_to='public_folder')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"file : {self.label}"


class BookCategory(models.Model):
    
    label = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Categorie Livre : {self.label}"

# class Book(models.Model):
    
#     label = models.CharField(max_length=120)
    
#     author = models.CharField(max_length=120)
    
#     code_isbn = models.CharField(max_length=120)
    
#     location = models.CharField(max_length=120, blank=True, blank=True)
    
#     attachement = models.FileField(upload_to='public_folder', blank=True)
    
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"file : {self.label}"