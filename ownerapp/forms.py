from django import forms
from ownerapp.models import Add_Ground


class Add_GroundForm(forms.ModelForm):
    class Meta:
        model = Add_Ground
        fields = "__all__"