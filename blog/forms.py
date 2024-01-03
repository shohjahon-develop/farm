from django import forms
from.models import Contact,New





class ContactForms(forms.ModelForm):


    class Meta:
        model = Contact
        fields = "__all__"

class NewForms(forms.ModelForm):


    class Meta:
        model = New
        fields = "__all__"























