from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y", height_field=100,width_field=100)
    def __str__(self):
        return self.caption
    def __format__(self):
        return self.caption[-1:-4]