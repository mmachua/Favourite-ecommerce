from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#class register(UserCreationForm):
 #   email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

  #  class Meta:
   #     model = User
    
    #    fields = ('username', 'email', 'password1', 'password2', )


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #super().__init__(strip=True, **kwargs)

    class Meta:
        model = User
        fields = ( 
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        User = super(RegistrationForm, self).save(commit=False)
        User.first_name = self.cleaned_data['first_name']
        User.last_name = self.cleaned_data['last_name']
        User.email = self.cleaned_data['email']

        if commit:
            User.save()

        return User


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )


class contactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True)