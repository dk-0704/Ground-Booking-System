from django import forms
from customerapp.models import Book_slot


class Book_slotForm(forms.ModelForm):
    class Meta:
        model = Book_slot
        fields = ["customer", "ground", "date", "time", "address", "description", "cost", "hours", "final_cost"]
