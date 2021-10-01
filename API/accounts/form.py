from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

from scraping import models

User=get_user_model()
class UserLoginForm(forms.Form):

    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean(self,*args,**kwargs):
        email=self.cleaned_data.get('email').strip()
        password=self.cleaned_data.get('password').strip()
        if email and password:
            qs=User.objects.filter(email=email)
        if not qs.exists():
            raise forms.ValidationError('Avtorizatsiya bomagansiz')
        if not check_password(password,qs[0].password):
            raise forms.ValidationError('Parol notogri terilgan')
        user=authenticate(email=email,password=password)
        if not user:
            raise forms.ValidationError('Activlashtirilmagan')
        return super(UserLoginForm,self).clean(*args,**kwargs)
class UserRegisterForm(forms.ModelForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='Email')
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Парол')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='павторить парол')
    class Meta:
        model=User
        fields=('email',)
    def clean_password2(self):
        data=self.cleaned_data
        if data['password']!=data['password2']:
            raise forms.ValidationError('passwordlar bir xil emas')
        return data['password2']
class UserUpdateForm(forms.Form):
    city = forms.ModelChoiceField(queryset=models.City.objects.all(), to_field_name='slug', required=True,
                                  widget=forms.Select(attrs={'class': 'form-select'}))
    language = forms.ModelChoiceField(queryset=models.Language.objects.all(), to_field_name='slug', required=True,
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    send_email=forms.BooleanField(widget=forms.CheckboxInput,required=False)

    class Meta:
        model=User
        field=('city','language','send_email')