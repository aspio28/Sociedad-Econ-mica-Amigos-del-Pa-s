from django import forms

class Form_Document(forms.Form):
    
    title = forms.CharField(label= "Titulo", required=True)
    author = forms.CharField(label="Autor", required=True)
    year = forms.IntegerField(label="Anho", required=True)
    document_type = forms.CharField(label="Tipo de Documento", required=True)
    body = forms.CharField(label="Cuerpo", required=True, widget=forms.Textarea)
