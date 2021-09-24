from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from cpf_field.validators import validate_cpf

from .models import Profile


class UserCreationFormCustom(UserCreationForm):
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Email...', }))
    username = forms.CharField(min_length=6, max_length=24,
                               widget=forms.TextInput(attrs={'placeholder': 'Username...'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        ValidationEmail = self.cleaned_data['email']

        if User.objects.filter(email=ValidationEmail).exists():
            raise ValidationError(f"O email {ValidationEmail} ja esta em uso")
        return ValidationEmail

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(f"Username {username} ja esta em uso.")

   
class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome...'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Sobrenome...','label':"Primeiro nome", }))
    CPF = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'placeholder': 'CPF...',}))
    
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'CPF')

    
    #descomnetar esse codigo em produção
    def clean_CPF(self):
        # validação de CPF
        CPF = self.cleaned_data['CPF']
        validate_cpf(CPF)
        if Profile.objects.exclude(CPF=CPF).exists():
            raise ValidationError(f"O CPF {CPF} ja esta em uso")
        return CPF
        
      