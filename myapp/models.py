from django.db import models

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self): # Este método es para que en el admin se muestre el nombre del proyecto
    return self.name


class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  project = models.ForeignKey(Project, on_delete=models.CASCADE)

  def __str__(self): # Este método es para que en el admin se muestre el nombre de la tarea
    return self.title + ' - ' + self.project.name # Aquí se muestra el nombre de la tarea y el nombre del proyecto al que pertenece