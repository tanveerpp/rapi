from django.db import models
class Emp(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    address=models.TextField()
    password=models.TextField(max_length=10)
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    cat=models.CharField(max_length=50)
    cmp=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
