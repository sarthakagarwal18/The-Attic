from django import forms
from .models import Review

#in built help for forms is given by ModelForm
class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Review
        fields = ('text',)