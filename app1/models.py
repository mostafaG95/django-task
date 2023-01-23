from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='photo/%y/%m/%d')
    description = models.TextField(max_length=100)
    model_choices=(('2010','2010'),('2015','2015'),('2020','2020'))
    model = models.CharField(max_length=20,choices=model_choices)
    class Meta:
        ordering=['name']
    # def __str__(self) -> str:
    #     return self.name
# Create your models here.
