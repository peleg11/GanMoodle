from django import forms
from activities.models import Activity

class ActivityForm(forms.ModelForm):
    
    class Meta:
        model = Activity
        fields = ('auther','title','text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }