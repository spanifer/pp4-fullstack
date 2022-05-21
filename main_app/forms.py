from django import forms
from .models import ViewingRequest


class ViewingRequestForm(forms.ModelForm):
    class Meta:
        model = ViewingRequest
        fields = ('fullname', 'phone', 'email', 'message')