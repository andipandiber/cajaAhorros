from django import forms

from django.contrib.auth import authenticate

from .models import User


class userRegisterForm(forms.ModelForm):

  password1 = forms.CharField(
    label = 'Password',
    required = True,
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Password'
        }
      )
    )

  password2 = forms.CharField(
    label = 'Password',
    required = True,
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Repeat Password'
        }
    )
  )

  class Meta:

    model = User
    fields = (
      'username',
      'email',
      'IDCard',
      'name',
      'last_name',
      'address',
      'phone',
      'dateBirth',
      )

  def clean_password2(self):
    if self.cleaned_data['password1'] != self.cleaned_data['password2']:
      self.add_error('password2', 'Password No coincide')

class loginUserForm(forms.Form):

    username = forms.CharField(
    label = 'username',
    required = True,
    widget = forms.TextInput(
        attrs = {
            'placeholder': 'Username'
        }
      )
    )
    password = forms.CharField(
    label = 'Password',
    required = True,
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Password'
        }
      )
    )

    def clean(self):
      cleaned_data = super(loginUserForm, self).clean()
      username = self.cleaned_data['username']
      password = self.cleaned_data['password']

      if not authenticate(username = username, password = password):
        raise forms.ValidationError('Los Datos de Usuario no son correctos')
        return self.cleaned_data

class updatePasswordForm(forms.Form):

  passwordCurrent = forms.CharField(
    label = 'Password Actual',
    required = True,
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Password Actual'
        }
      )
    )

  passwordNew = forms.CharField(
    label = 'Password Nuevo',
    required = True,
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Nuevo Password'
        }
    )
  )


class verifyUserForm(forms.Form):
  codeRegistration = forms.CharField(required = True)

  def __init__(self, pk, *args, **Kwargs):
    self.id_user = pk
    super(verifyUserForm, self).__init__(*args, **Kwargs)


  def clean_codeRegistration(self):
    code = self.cleaned_data['codeRegistration']

    if len(code) == 6:
      active = User.objects.codeValidator(self.id_user, code)
      
      if not active:
        raise forms.ValidationError('El Codigo es Incorrecto')
    else:
      raise forms.ValidationError('El Codigo es Incorrecto')
