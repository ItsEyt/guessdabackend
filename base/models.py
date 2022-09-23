from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class folder(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class image(models.Model):
    folder = models.ForeignKey(folder, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='frames', default=NULL)
