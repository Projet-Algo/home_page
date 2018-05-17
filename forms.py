from django import forms


class ContactForm(forms.Form):

    utilisateur = forms.CharField(max_length=100)
    email = forms.EmailField(label="Votre adresse e-mail")
    Password = forms.CharField(widget=forms.PasswordInput)