from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django_countries.fields import CountryField
from crispy_bootstrap5.bootstrap5 import FloatingField
from django_countries.widgets import CountrySelectWidget
from clients.models import CustomUser
from django.urls import reverse



class SelfLoginForm (LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["login"] = forms.CharField(label='user ID')
        self.fields["login"].widget.attrs.update(
            {'class': 'form-control-lg rounded-4  mb-4'})
        self.fields["password"].widget.attrs.update(
            {'class': 'form-control-lg rounded-4 mb-4 '})
        
    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('profile', kwargs={'username': self.request.user.username})
    
        
class TransferForm(forms.Form):
    beneficiary_bank_address = forms.CharField(widget=forms.Textarea(attrs={'rows':'3'}))
    pin = forms.IntegerField()
    amount = forms.DecimalField()
    swift_code = forms.CharField(max_length=34, required=False)
    receivers_name = forms.CharField(max_length=30)
    beneficiary_account_number = forms.CharField(max_length=15)
    description = forms.CharField(max_length=150)
    country = CountryField(blank_label="(Select country)").formfield(widget =  CountrySelectWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        self.fields["amount"].widget.attrs.update(  
            {'class': 'form-control-lg '})
        self.fields['amount'].label = 'Amount $'
        
        self.fields["country"].widget.attrs.update(
            {'class': 'form-control-lg rounded-4'})
        self.fields["pin"].widget.attrs.update(
            {'class': 'form-control-lg rounded-4'})
        self.fields["swift_code"].widget.attrs.update(
            {'class': 'form-control-lg rounded-4'})
        self.fields["receivers_name"].widget.attrs.update(
            {'class': 'form-control-lg rounded-4'})
        self.fields["beneficiary_account_number"].widget.attrs.update(
            {'class': 'form-control-lg rounded-4'})
        # self.fields["description"].widget.attrs.update(
        #     {'class': 'form-control-lg rounded-4'})
        

class DeactivateUser(forms.Form):
    deactivate = forms.BooleanField()


class CardRequestForm(forms.Form):
    cardTypes = (
        ('gold', 'GOLD'),
        ('infinite', 'INFINITE'),
        ('platinum', 'PLATINUM')
    )
    cardtype = forms.ChoiceField(choices=cardTypes, widget=forms.RadioSelect(attrs={"class": "test", "required": True}), required=True)