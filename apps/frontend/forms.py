from django import forms


class EmployeeAddForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    age = forms.IntegerField(min_value=1)
    department = forms.IntegerField(min_value=1)
    language = forms.IntegerField(min_value=1)
