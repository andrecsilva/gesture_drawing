from django import forms

from .models import Tag

class SessionForm(forms.Form):
    ref_count = forms.IntegerField(initial=10,label='Enter a non-negative integer here',min_value=1);
    tags_filter = forms.ModelMultipleChoiceField(label='Restric to specific tags (union):',queryset=Tag.objects.all(),required=False);

class NewTagForm(forms.Form):
    tag_name = forms.CharField(min_length=1,strip=True);
    tag_description = forms.CharField(min_length=1,strip=True);
