from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email","password1","password2")

    def save(self, commit = True) :
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class FormSearch(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Titulo'}), required=True)
    author = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Autor'}), required=True)
    year = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Anho en que fue escrito'}), required=True)
    document_type = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'input-field','placeholder':'Tipo de documento'}), required=True)
