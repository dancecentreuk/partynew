from django.db import models

# Create your models here.


class Style(models.Model):
    dance_style = models.CharField(max_length=200, help_text='Enter Dance Style')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.dance_style
