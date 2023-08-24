from allauth.account.forms import SignupForm, LoginForm
from django import forms



class SelfLoginForm (LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["login"] = forms.CharField(label='user ID')
        self.fields["login"].widget.attrs.update(
            {'class': 'form-control-lg rounded-4  mb-4'})
        self.fields["password"].widget.attrs.update(
            {'class': 'form-control-lg rounded-4 mb-4 '})