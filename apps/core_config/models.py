from django.db import models
# Create your models here.


class Config(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    type = models.CharField(max_length=200,)
    slogan = models.ImageField(upload_to='slogan/images',blank=True)
    
    def __str__(self):
        return self.name

