from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    # підпис
    def __str__(self):
        return self.caption
    # тип картинки
    def __format__(self):
        return self.image.name.rsplit(".")[1]