from django import forms
from django.contrib.auth.models import User
from . import models



class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('profile_img', )
        model = models.Profile
