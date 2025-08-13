from django import forms
from .models import ContactUs


from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'family', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'}),
            'family': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
