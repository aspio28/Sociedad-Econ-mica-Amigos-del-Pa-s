from django import forms

class Form_Document(forms.Form):
    
    title = forms.CharField(label= "", widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Titulo'}), required=True)
    author = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Autor'}),  required=True)
    year = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Año en que fue escrito'}), required=True)
    document_type = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Tipo de documento'}), required=True)
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'class' : 'input-field','rows':3, 'cols':5,'placeholder':'Documento'}), required=True)

class FormSearch(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Titulo', 'name':'tit'}), required=False)
    author = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Autor', 'name':'aut'}), required=False)
    year = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Anho en que fue escrito', 'name':'year'}), required=False)
    document_type = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Tipo de documento', 'name':'type'}), required=False)
