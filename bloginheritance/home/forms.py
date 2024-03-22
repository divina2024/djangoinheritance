
from django import forms
from .models import Article

class form1(forms.ModelForm): 
    class Meta: 
        model = Article 
        fields = "__all__"
