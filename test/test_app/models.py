from django.db import models

# Create your models here.
class TestModel(models.Model):
    test_field = models.CharField(max_length=50, default="")
    