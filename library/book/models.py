from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length= 50)
    author = models.CharField(max_length=25)
    publisher = models.CharField(max_length=25)
    borrow = models.BooleanField(default=0)
    publication_year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    