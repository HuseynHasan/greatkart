from django import forms
from .models import Account

# qrDc@2tFNC5GrGF , johndoe80@gmail.com
# ArDc@2tFNC5GrGF , donladtrump79@gmail.com
# BrDc@2tFNC5GrGF , jonidom@gmail.com
# crDc@2tFNC5GrGF , conitravolta@gmail.com
# ErDc@2tFNC5GrGF , contravolta@gmail.com
# orDc@2tFNC5GrGF , brendemlak@gmail.com
# krDc@2tFNC5GrGF , jby@gmail.com


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password',
        'class' : 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password',
    }))
    class Meta:
        model  = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

