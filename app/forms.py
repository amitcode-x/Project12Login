from django import forms

from app.models import *



class UserMF(forms.ModelForm):
    class Meta:
        model = User
        
        # fields = "__all__"
        fields = ["username", "email", "password"]
        help_texts ={'username': None}
        
class ProfileMF(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = "__all__"
        fields =["profile_pic", "address"]