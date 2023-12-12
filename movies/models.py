from django.db import models

# Create your models here.
class Movies(models.Model):
  img = models.FileField(upload_to="books/cover",null=True,blank=True)
  des = models.CharField(max_length=255)
  name = models.CharField(max_length=30,null=True)

  def __str__(self):
      return self.name