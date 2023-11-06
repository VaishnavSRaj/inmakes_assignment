from django import forms
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password'
    }))

    class Meta:
        model = CustomUser
        fields = ['username',  'password', 'confirm_password']
    def __init__(self ,*args, **kwargs):
        super(UserRegistrationForm,self).__init__(*args , **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Enter username'

    def clean(self):
        clean_data=super(UserRegistrationForm , self).clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        if password!=confirm_password:
            raise forms.ValidationError(
                'Password does not match !'
            )


