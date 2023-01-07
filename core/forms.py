from django import forms
from django.core.exceptions import ValidationError
class WaitlistForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'waitlist', 'placeholder': 'Enter your email address'}) ,required=True, label="")

class ContactForm(forms.Form):
    name= forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'placeholder': 'John Doe'}) ,min_length=2, required=True, label="Your name", label_suffix="")
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'name@email.com'}) ,required=True, label="Your email", label_suffix="")
    subject= forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Let us know how we can help you'}), min_length=2, required=True, label="Subject", label_suffix="")
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : 'Leave a comment...', 'class' : 'input', 'rows': '6', 'cols': '12'}), label="Your message", label_suffix="")

    def clean_fields(self):
        cd = self.cleaned_data
        valid = self.is_valid()
        if cd and valid:
            return self
        return forms.ValidationError('Somethin went wrong')