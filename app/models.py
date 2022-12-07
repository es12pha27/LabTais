from django.db import models

# Create your models here.
class Taller(models.Model):
    creacion=models.DateTimeField(auto_now_add=True)
    titulo=models.CharField(max_length = 150)
    descripcion=models.TextField()
    ponente=models.CharField(max_length = 180)
    lugar=models.CharField(max_length = 200)
    duracion=models.CharField(max_length =15, default="1 hora")

    def __str__(self):
        return self.titulo