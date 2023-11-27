from django.db import models
from datetime import datetime    
from django.utils.timezone import now 
from django.contrib.auth.models import User 
# Create your models here.


class book_model(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null = True , blank = True)
    uploaded_by = models.CharField(max_length = 100 , null = True)
    title = models.CharField(null=False , max_length = 100)
    ISBN = models.CharField(max_length=20)
    upload_date = models.DateField(auto_now_add=True)
    publication_date = models.DateField(auto_now_add=False)
    book_description = models.TextField(max_length= 500 , default="Hello")
    book_image = models.ImageField(upload_to="imgs" , default = "imgs/default_img.png")
    file = models.FileField(upload_to="books") 
