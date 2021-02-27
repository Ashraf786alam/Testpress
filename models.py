from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class mark(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    math=models.IntegerField(default=0)
    english=models.IntegerField(default=0)
    physics=models.IntegerField(default=0)
    chemistry=models.IntegerField(default=0)
    biology=models.IntegerField(default=0)
    social=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    def __str__(self):
        return self.name
