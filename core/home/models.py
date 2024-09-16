from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null = True, blank=True)
    # image = models.ImageField()
    file = models.FileField(null=True)

## these are some example of fields ,,, there are many more fields available to use...


class Car(models.Model):
    car_name = models.CharField(max_length=20)
    speed = models.IntegerField(default=20)

    def __str__(self) -> str:
        return self.car_name
        
    