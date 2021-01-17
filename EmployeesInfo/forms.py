
from django.forms import ModelForm
from Employees.models import employees

class AddForm(ModelForm):
    class Meta:
        model=employees
        fields=('Email','FirstName','LastName')