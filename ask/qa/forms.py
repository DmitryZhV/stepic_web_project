from django import forms
from django.forms import ModelForm

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_text(self):
        text = self.clean




class AnswerForm(forms.Form):
    text = 
