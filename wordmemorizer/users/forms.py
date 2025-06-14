from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from .models import Word  # Word modelini oluşturacağız

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class AddWordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['kelime', 'anlam']  # Modeldeki alan adları