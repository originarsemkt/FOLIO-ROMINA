from django.db import models

# Create your models here.
#modelo para formacion  = course
class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    degree_title = models.CharField(max_length=300,verbose_name='Titulo obtenido')
    descripción = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Modificación')
    
#Pasos para convertir la aplicacion de admin en español, como se crea de forma ascendente
class Meta:
    verbase_name = 'formación'
    verbase_name_plural = 'formaciones'
    ordering = ['-created']                    

#muestro en la lista de proyectos de admin, todos los proyectos con su titulo


#modelo para conocimientos = skill
class Skill(models.Model):
    title = models.CharField(max_length=80, verbose_name='Titulo')
    image = models.ImageField(upload_to='skills', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Modificación')
    
class Meta:
    verbase_name = 'conocimiento'
    verbase_name_plural = 'conocimientos'
    ordering = ['-created']   
    
#Con esta funcion muestra por titulo
def __str__(self):
    return self.titulo
        
