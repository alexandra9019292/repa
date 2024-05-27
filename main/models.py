from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    img = models.ImageField()

    avtors = models.ForeignKey('Avtor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Avtor(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    img = models.ImageField()

    avtors = models.ForeignKey('Avtor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


