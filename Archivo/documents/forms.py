from django import forms

class Form_Document(forms.Form):
    
    title = forms.CharField(label= "Titulo", required=True)
    author = forms.CharField(label="Autor", required=True)
    body = forms.CharField(label="Cuerpo", required=True, widget=forms.Textarea)