from django.db import models

# Create your models here.
# DB와 연결되는 python 의 class

class Post(models.Model):
    title=models.CharField(max_length=64)
    user=models.CharField(max_length=32)
    content=models.TextField() #글자수 제한 X
    region=models.CharField(max_length=16)
    price=models.IntegerField()

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
