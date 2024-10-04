from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')  # Залежно від вашої структури

    def __str__(self):
        return self.title
