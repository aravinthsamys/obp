from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username','style':'border: none;outline: none;width:fit-content;'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mail Address','style':'border: none;outline: none;width:fit-content;'}))
    password1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Password','style':'border: none;outline: none;width:fit-content;'}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm Password','style':'border: none;outline: none;width:fit-content;'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']


class CustomPassResetForm(UserCreationForm):
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-field','style':'width: 100%;padding: 10px;text-align: center;border-radius: 10px;'}))
    class Meta:
        model=User
        fields=['email']

class CustomPassConfirmForm(UserCreationForm):
    new_password1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'width:20%;height:40px;background:white;border:none;outline:none;font-size:1em;color:black;padding:0 35px 0 5px;'}))
    new_password2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'width:20%;height:40px;background:white;border:none;outline:none;font-size:1em;color:black;padding:0 35px 0 5px;'}))

    class Meta:
        model=User
        fields=['new_password1','new_password2']

class ImageForm(forms.ModelForm):
    class Meta:
        model = businessdata
        fields = ['username_post','owner_name','gender','company_name','description','category','gstin_number','reg_number','city','street_address','town_address','pincode','contact_number','email_id','image','website_link','gmaps_link','business_work_type']


# class profileupdateform(forms.ModelForm):
#     class Meta:
#         model=businessdata
#         field=['photocopy']
# import pymysql # type: ignore
# pymysql.install_as_MySQLdb()