from django import forms
from demoapp.models import *

class QuizModelForm(forms.ModelForm):
    class Meta:
        model = QuizModel
        fields = '__all__'
