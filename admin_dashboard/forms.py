from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from clients.models import CustomUser
from allauth.account.forms import SignupForm, LoginForm
from django_countries.fields import CountryField
from crispy_bootstrap5.bootstrap5 import FloatingField



class DateInput(forms.DateInput):
    input_type = 'date'

gender = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('non binary', 'NON BINARY')
)

class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'name@example.com'}))
    balance = forms.DecimalField(max_digits=10, decimal_places=2)
    address = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':'5'}))
    country = CountryField(blank=False).formfield()
    dob = forms.DateField(widget=DateInput)
    gender = forms.ChoiceField(choices=gender)
    image = forms.ImageField(required=False)

    def save(self, request):
        CustomUser = super(MyCustomSignupForm, self).save(request)     
        CustomUser.country = self.cleaned_data['country']
        CustomUser.address = self.cleaned_data['address']
        CustomUser.save() 
        
        return CustomUser

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        # super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                FloatingField("first_name", wrapper_class='col-md-6', css_class="row-fluid"),
                FloatingField("last_name", wrapper_class='col-md-6', css_class="row-fluid"),
            ),
            Row(
                FloatingField("email", wrapper_class='col-md-6', css_class="row-fluid"),
                FloatingField("username", wrapper_class='col-md-6', css_class="row-fluid"),
            ),
            Row(
                FloatingField("password1", wrapper_class='col-md-6', css_class="row-fluid"),
                FloatingField("password2", wrapper_class='col-md-6', css_class="row-fluid"),
            ),

            Row(
                FloatingField("balance", wrapper_class='col-md-3', css_class="row-fluid"),
                FloatingField("country", wrapper_class='col-md-3', css_class="row-fluid"),
                FloatingField("dob", wrapper_class='col-md-3', css_class="row-fluid"),
                FloatingField("gender", wrapper_class='col-md-3', css_class="row-fluid"),
            ),
            FloatingField('address'),
            FloatingField('image', wrapper_class="col-md-6"),
            Submit('submit', 'CREATE ACCOUNT', css_class="mt-5 col-12 col-md-5")
            

        )


class ClientUpdateForm(forms.ModelForm):
    country = CountryField().formfield()
    dob = forms.DateField(widget=DateInput)
    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name', 'address', 'country', 'dob', 'mobile_number', 'image']


class DeactivateUser(forms.Form):
    deactivate = forms.BooleanField()