from django.db import models
from django.db.models.fields import CharField, URLField  # Importar solo CharField, no es necesario calificar con models.
from django.db.models.fields.files import ImageField

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/image')
    url = models.URLField(blank=True)