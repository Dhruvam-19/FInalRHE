from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Information
from django.core.files.uploadedfile import SimpleUploadedFile
class DateInput(forms.DateInput):
    input_type = 'date'

class Userregisterform(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Profile_form(forms.ModelForm):
    # profile_picture = forms.ImageField(label='Profile Picture')
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    # middle_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Middle name'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    # father_first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Father/Husband First name'}))
    # father_middle_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Father/Husband Middle name'}))
    # father_last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Father/Husband Last name'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    # phone_number1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number1'}))
    # phone_number2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number2'}))
    # address_lane1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address lane1'}))
    # address_lane2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address lane2'}))
    # address_lane3 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address lane3'}))
    # state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'State'}))
    # bank_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Bank Name'}))
    # bank_branch = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Branch Name'}))
    # pan_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pan Number'}))
    # account_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Account number'}))
    # micr_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'MICR code'}))
    # ifsc_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ifsc code'}))
    # country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    # adharcard_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Aadharcard Number'}))
    # date_of_birth = forms.DateField(widget=DateInput(attrs={'placholder':'Birth Date'}))
    # joining_date = forms.DateField(widget=DateInput(attrs={'placholder': 'Joining Date'}))
    # resignation_date = forms.DateField(widget=DateInput(attrs={'placeholder': 'Resignaiton date'}))
    # execution = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Execution'}))
    # bd = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'BD'}))
    # agreement_document = forms.ImageField(label='Agreement Document')
    # document1 = forms.ImageField(label='Document1')
    # document2 = forms.ImageField(label='Document2')
    # document3 = forms.ImageField(label='Document3')

    class Meta:

        model = Information
        fields = ['profile_picture','first_name','middle_name','last_name',
                  'father_first_name','father_middle_name',
                  'father_last_name','address_lane1','address_lane2',
                  'state','ifsc_code','email','phone_number1','phone_number2',
                  'address_lane3','country','bank_name','bank_branch',
                  'pan_number','account_number','micr_code','adharcard_number',
                  'date_of_birth','joining_date','resignation_date','execution',
                  'bd','agreement_document','document1','document2','document3'
                  ]

        def __init__(self, *args, **kwargs):
            super(Profile_form, self).__init__(*args, **kwargs)
            self.fields['profile_picture'].required = False
            self.fields['document1'].required = False
            self.fields['document2'].required = False
            self.fields['document3'].required = False
