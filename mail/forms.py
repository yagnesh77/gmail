from django import forms


class ContactForm(forms.Form):
  name =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
  email = forms.EmailField(required=True)
  