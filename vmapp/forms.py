from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import VehicleDtls


  
class SignUpForm(UserCreationForm):
    USER_ROLE_TYPE =(
    ("1","Super Admin"),
    ("2","Admin"),
    ("3","User"),    
)
    email = forms.EmailField(required=True)
    user_mode  = forms.ChoiceField(choices = USER_ROLE_TYPE)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "user_mode"]


class VehicleDtlsForm(forms.ModelForm):
    class Meta:
        model = VehicleDtls
        fields = ["Vehicle_Number", "Vehicle_Type", "Vehicle_Model", "Vehicle_Description"]



