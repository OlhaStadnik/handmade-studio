from django import forms
from studio.models import Jewelry, Master
from django.contrib.auth.forms import UserCreationForm

class JewelryForm(forms.ModelForm):
    class Meta:
        model = Jewelry
        fields = '__all__'


class MasterCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Master
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "experience_years", "biography",)