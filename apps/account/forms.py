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
    #CPF = forms.CharField(max_length=11, required=False, widget=forms.TextInput(attrs={'placeholder': 'CPF...'}))
    
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
        raise forms.ValidationError(u'Username "%s" is already in use.' % username)

    # def clean_cpf(self):
    #     CPF = self.cleaned_data['CPF']
    #     try:
    #         validate_cpf(CPF)
    #         if Profile.objects.filter(CPF=CPF).exists():
    #             raise ValidationError(f"O cpf {CPF} ja esta em uso")
    #     except Profile.DoesNotExist:
    #         return CPF
    #     raise forms.ValidationError("CPF invaldio")
