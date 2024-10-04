from django.db import models

# Create your models here.

class Manual(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='manual_images/', blank=True, null=True)
    manual_file = models.FileField(upload_to='manuals/', blank=True, null=True)
    
    def __str__(self):
        return self.title