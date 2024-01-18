from django import forms
from home.models import Post


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)

class HomeCreate(forms.ModelForm):
    bizname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write the business name here...'
        }
    ))
    location = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write the location of the business here...'
        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write the phone number to your business here...'
        }
    ))

class ContactForm(forms.Form):
    Name = forms.CharField(required=True,max_length=25, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your name here 25 characters max...'
        }
    ))
    Email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={
            
            'placeholder': 'Write your email address here...'
        }
    ))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your message here...'
        }
    
    ))
    

#class ContactForm(forms.ModelForm):
#    contact_name = forms.CharField(required=False, max_length=100)
#    contact_email = forms.EmailField(required=True)
