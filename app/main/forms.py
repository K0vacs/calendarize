from django import forms

# Adding a static contact form
class ContactForm(forms.Form):
    full_name = forms.CharField(       
        required=True, 
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Full Name',
            }
        )
    )
    email_address = forms.EmailField(
        required=True, 
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
            }
        )
    )
    
    message = forms.CharField(
        required=True, 
        label="", 
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Message',
                'rows': 4,
            }
        )
    )