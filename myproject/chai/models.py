from django.db import models
from django.utils import timezone

# Create your models here.

class chaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala Chai'),
        ('GR', 'Green Tea'),
        ('BL', 'Black Tea'),
        ('HE', 'Herbal Tea'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

def __str__(self):
  return self.name