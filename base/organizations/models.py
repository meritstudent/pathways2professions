from django.db import models

# Create your models here.
class Organization(models.Model):  
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=50)

# class Favorite(models.Model):
#     _org = models.ForeignKey(to=Organization, on_delete=models.CASCADE)

class Tag(models.Model):
    CTE_area = models.CharField( max_length=50)

class OTRelation(models.Model):

    _tag =models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    _org =models.ForeignKey(to=Organization, on_delete=models.CASCADE)
