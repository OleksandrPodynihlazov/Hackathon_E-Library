from django.contrib import admin
from .models import Manual, Quiz, Question, Choice

# Register your models here.
admin.site.register(Manual)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)