from django import forms

class UpdateStatus(forms.Form):
    status = forms.CharField(max_length=100, help_text="Enter the current status.")
