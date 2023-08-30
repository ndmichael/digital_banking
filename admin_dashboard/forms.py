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
    field_order = ['first_name', 'last_name',  'username',
                   'email', 'password1', 'password2', 'balance','country', 'address', 'dob','image']
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'name@example.com'}))
    balance = forms.DecimalField(max_digits=10, decimal_places=2)
    address = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':'5'}))
    country = CountryField(blank=True).formfield()
    dob = forms.DateField(widget=DateInput)
    gender = forms.ChoiceField(choices=gender)
    image = forms.ImageField(required=False)

    def save(self, request):
        CustomUser = super(MyCustomSignupForm, self).save(request)
        CustomUser.first_name = self.cleaned_data['first_name']
        CustomUser.last_name = self.cleaned_data['last_name']
        CustomUser.save()
        # number = [randrange(10) for i in range(10)]
        # acc_number = ''.join(str(i) for i in number)
        # pin = acc_number[:4]
        # models.Client.objects.create(
        #         user=user, 
        #         balance=self.cleaned_data['balance'], 
        #         address=self.cleaned_data['address'], 
        #         country=self.cleaned_data['country'], 
        #         dob=self.cleaned_data['dob'],
        #         gender = self.cleaned_data['gender'],
        #         account_number = acc_number,
        #         transfer_pin = pin,
        #         active = True

        # )
        # return user

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