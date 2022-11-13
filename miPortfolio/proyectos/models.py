from django.db import models

# Create your models here.

class Proyectos(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    titulo = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True, db_column='imagen')  # Field name made lowercase. This field type is a guess. 
    titulodos = models.TextField(db_column='tituloDos', blank=True, null=True)  # Field name made lowercase.
    linkp = models.TextField(db_column='linkP', blank=True, null=True)
    linkr = models.TextField(db_column='linkR', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectos'