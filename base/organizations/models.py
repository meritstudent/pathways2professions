from django.db import models

# Create your models here.
class Organization(models.Model):  
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    description = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# class Favorite(models.Model):
#     _org = models.ForeignKey(to=Organization, on_delete=models.CASCADE)

class Tag(models.Model):
    CTE_area = models.CharField( max_length=50)
    def __str__(self):
        return self.CTE_area

    class Meta:
        ordering = ['CTE_area']

class OTRelation(models.Model):

    _tag =models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    _org =models.ForeignKey(to=Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self._org.__str__() +" #"+ self._tag.__str__()
