from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

#1 to many
class chaiReveiw(models.Model):
    chai = models.ForeignKey(chaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
#many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    chai_varities = models.ManyToManyField(chaiVarity, related_name='stores')

    def __str__(self):
        return self.name
    

#1 to 1
class chacertificte(models.Model):
    chai = models.OneToOneField(chaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issue_date = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'