from django import forms

# clase definir los datos del alumnos

class Alumno(forms.Form):
    #definir los datos
    codigo=forms.CharField()
    nombre=forms.CharField()
    curso=forms.ChoiceField()
    parcial=forms.IntegerField()
    practica=forms.IntegerField()
    final=forms.IntegerField()
