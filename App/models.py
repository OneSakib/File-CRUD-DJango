from django.db import models


# Create your models here.
class Data(models.Model):
    file = models.FileField(upload_to='file/')
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.desc[:20]
