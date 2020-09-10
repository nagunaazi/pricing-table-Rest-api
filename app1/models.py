from django.db import models

# Create your models here.

class PricingTable(models.Model):
    ID = models.IntegerField(primary_key=True)
    Plan_Name= models.CharField(max_length=30)
    Plan_Formula=models.CharField(max_length=30)
    Location=models.CharField(max_length=30)
    Plan_Status=models.CharField(max_length=30)
    Created_Date=models.DateField()
    Updated_Date=models.DateField()


from rest_framework import  serializers

class PrincingTablesSerializer(serializers.ModelSerializer):
    class Meta:
        model=PricingTable
        fields="__all__"


