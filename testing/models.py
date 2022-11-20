from django.db import models

# Create your models here.

class people(models.Model):
    POSITIONS=(
        ('CEO', 'CEO'),
        ('CHAIRPERSON', 'CHAIRPERSON'),
        ('DEVELOPER', 'DEVELOPER'),
        ('SPONSOR', 'SPONSOR'),
    )

    first_name   = models.CharField(max_length=40)
    last_name    = models.CharField(max_length=40)
    position     = models.CharField(max_length=40, choices=POSITIONS)
    person_image = models.ImageField(upload_to='media/people/')

    def __str__(self):
        return self.last_name

class goods(models.Model):
    NATURE = (
        ('NEW', 'NEW'),
        ('REFURBISHED', 'REFURBISHED'),
    )

    name           = models.CharField(max_length= 40)
    image          = models.ImageField(upload_to='media/goods/')
    descriptions   = models.TextField()
    condition      = models.CharField(max_length=40, choices=NATURE)
    price          = models.IntegerField()

    def __str__(self):
        return self.name
