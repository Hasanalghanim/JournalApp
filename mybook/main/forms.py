from django.forms import ModelForm, Textarea
from .models import Entry




class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['Title','Journal']
        widgets = {
        'Title':Textarea(attrs={'class':'materialize-textarea'}),
        'Journal':Textarea(attrs={'class':'materialize-textarea'})
        }
