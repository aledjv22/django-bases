from django import forms

class CreateNewTask(forms.Form):
  title = forms.CharField(label="Titulo de tarea", max_length=200)
  description = forms.CharField(label="descripción de la tarea",widget=forms.Textarea)