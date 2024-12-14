from django import forms
from groundapp.models import Contact, Customer, Owner


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = "__all__"

