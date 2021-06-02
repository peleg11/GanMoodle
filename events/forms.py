from django import forms
from events.models import Event

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ('auther','name','date','attendees','discription')
        widgets = {
            'name':forms.TextInput(attrs={'class':'textinputclass'}),
            'discription':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'date':DateInput(),
        }