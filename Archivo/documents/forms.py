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
    
    # def __init__(self, *args,**kwargs):
    #     xml_file = kwargs.pop('xml_file',None)
    #     super().__init__(*args,**kwargs)
    #     if xml_file:
    #         tree = ET.parse(xml_file)
    #         root = tree.getroot()
    #         self.initial['title'] = root.find('titulo').text
    #         self.initial['author'] = root.find('autor').text
    #         self.initial['year'] = root.find('anho_en_que_fue_escrito').text
    #         self.initial['document_type'] = root.find('tipo_de_documento').text
    #         self.initial['body'] = root.find('cuerpo').text

    # def clean(self):
    #     xml_file = self.cleaned_data('xml_file')
    #     if xml_file:
    #         tree = ET.parse(xml_file)
    #         root = tree.getroot()
    #         self.cleaned_data['title'] = root.find('title').text
    #         self.cleaned_data['author'] = root.find('author').text
    #         self.cleaned_data['year'] = root.find('year').text
    #         self.cleaned_data['document_type'] = root.find('document_type').text
    #         self.cleaned_data['body'] = root.find('body').text
    #     return self.cleaned_data

    # def clean(self):
    #     # xml_file = self.cleaned_data.get('xml_file')
    #     # title = self.cleaned_data.get('title')
    #     # author = self.cleaned_data.get('author')
    #     # year = self.cleaned_data.get('year')
    #     # doc_type = self.cleaned_data.get('document_type')
    #     # body = self.cleaned_data.get('body')

    #     # if(xml_file and title or author or year or doc_type or body):
    #     #     raise ValidationError("Solo ingrese un valor")
    #     # return self.cleaned_data
    # # #     # Form_Document.is_valid(self)
    # # #     # cleaned_data=super().clean()
    # # #     # if 'xml_file' not in self.files:
    # # #     #     if not cleaned_data.get('title') or not cleaned_data.get('author') or not cleaned_data.get('year'):
    # # #     #         raise forms.ValidationError("Debes llenar algo")
    # # #     # return cleaned_data
    #     if all(value is None for value in self.cleaned_data.values()):
    #         raise ValidationError("Debe ingresar un XML o llenar los campos")

    #     xml_file = self.cleaned_data.get('xml_file')
    #     if(xml_file is None):
    #         self.fields['title'].required = False
    #         self.fields['author'].required = False
    #         self.fields['year'].required = False
    #         self.fields['document_type'].required = False
    #         self.fields['body'].required = False

class FormSearch(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Titulo', 'name':'tit'}), required=False)
    author = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Autor', 'name':'aut'}), required=False)
    year = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Anho en que fue escrito', 'name':'year'}), required=False)
    document_type = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Tipo de documento', 'name':'type'}), required=False)
