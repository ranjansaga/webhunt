from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'key-text'}))
    firstName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'key-text'}))
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'key-text'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))
    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'key-text'}))

class ContactForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))

