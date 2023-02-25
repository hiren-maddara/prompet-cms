from django import forms
from .models import Diese


class form1(forms.Form):
    Customername=forms.CharField(max_length=200,widget=forms.TextInput())
    Telephonecontact=forms.CharField(max_length=200,widget=forms.TextInput())
    Date=forms.DateField(widget=forms.TextInput())
    EmployeeName=forms.CharField(max_length=200,widget=forms.TextInput())
    EmployeeAddress=forms.CharField(max_length=200,widget=forms.TextInput())
    Fueltype=forms.CharField(max_length=200,widget=forms.TextInput())
    AmountinLitres=forms.CharField(max_length=200,widget=forms.TextInput())
    UnitPrice=forms.CharField(max_length=200,widget=forms.TextInput())
    TotalPrice=forms.CharField(max_length=200,widget=forms.TextInput())

    # class Meta:
    #     model=Diese
    #     fields=['Customername','Telephonecontact','Date','EmployeeName',' EmployeeAddress','','Fueltype','AmountinLitres','UnitPrice','TotalPrice']