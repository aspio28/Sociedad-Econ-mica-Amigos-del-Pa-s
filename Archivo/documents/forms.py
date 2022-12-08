from django import forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import xml.etree.ElementTree as ET

class Form_Document(forms.Form):
    xml_file = forms.FileField(validators=[FileExtensionValidator(['xml'])], widget=forms.FileInput(attrs={'class' : 'input-field','placeholder':'Seleccione el archivo XML'}),required=False)
    title = forms.CharField(label= "", widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Titulo'}),required=False)
    author = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Autor'}),required=False)
    year = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Año en que fue escrito'}),required=False)
    document_type = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Tipo de documento'}),required=False)
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'class' : 'input-field','rows':3, 'cols':5,'placeholder':'Documento'}),required=False)
    

class FormSearch(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Titulo', 'name':'tit'}), required=False)
    author = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Autor', 'name':'aut'}), required=False)
    year = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Anho en que fue escrito', 'name':'year'}), required=False)
    document_type = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Tipo de documento', 'name':'type'}), required=False)
