from django.db import models

# This model is the BaseModel
class Model1(models.Model):
    field1 = models.CharField(max_length=50, null=True)
    field2 = models.CharField(max_length=50, null=True)
    field3 = models.IntegerField(null=True)
    field4 = models.IntegerField(null=True)

# This is inheriting from Model1
class Model2(Model1):
    field5 = models.CharField(max_length=100)
    field6 = models.IntegerField()
    field7 = models.CharField(max_length=150)

# This also inherit form Model1
class Model3(Model1):
    field8 = models.IntegerField()
    field9 = models.CharField(max_length=200)
    field10 = models.ForeignKey(Model2, on_delete=models.CASCADE)
