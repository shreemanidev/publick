from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Join(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=20,default="")
    pan = models.FileField(upload_to='uploads',default="", null=True, blank=True)
    aadhar = models.FileField(upload_to='uploads',default="", null=True, blank=True)
    photo = models.ImageField(upload_to='uploads',default="", null=True, blank=True)
    certificate = models.FileField(upload_to='uploads',default="", null=True, blank=True)

    def __str__(self):
        return self.name