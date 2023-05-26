from django.db import models

# Create your models here.

class Genres(models.Model):
    genre=models.CharField(max_length=120,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.genre


class Movies(models.Model):
    name=models.CharField(max_length=250,unique=True)
    genre=models.ManyToManyField(Genres,null=True)
    year=models.CharField(max_length=200)
    options=(
        ("Malayalam","Malayalam"),
        ("Telungu","Telungu"),
        ("Tamil","Tamil"),
        ("English","English"),
        ("Hindi","Hindi")
    )
    language=models.CharField(max_length=200,choices=options,default="Malayalam")
    runtime=models.FloatField()
    poster_image=models.ImageField(upload_to="Images",null=True,blank=True)
    description=models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.name





