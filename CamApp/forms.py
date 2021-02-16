from django import forms
from django.forms import widgets
from .models import Camera

class CamForm(forms.ModelForm):
    CHOICES=[('select1','select 1'),
         ('select2','select 2')]
    class Meta:
        
        model = Camera
        fields = '__all__'
        widgets = {
            'cam_url' : forms.URLInput(attrs={'class':'input--style-4'}),
            'stream_status':forms.Select(attrs={'class':'input--style-4'}),
            'cam_model' : forms.TextInput(attrs={'class':'input--style-4'}),
            'created_at' : forms.DateInput(attrs={'class':'input--style-4 js-datepicker'}),
            'cam_name' : forms.TextInput(attrs={'class':'input--style-4'}),
            'cam_user' : forms.TextInput(attrs={'class':'input--style-4'}),
            'cam_group' : forms.Select(attrs={'class':'input--style-4'}),
            
        }
        # stream_status = forms.CharField(widget=forms.PasswordInput(attrs={'class':'hi'}))
