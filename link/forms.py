from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = {
            'starting_block',
            'ending_block',
            'creator',
            'warrant'
        }

    def save(self, commit=True):
        link = super(forms.ModelForm, self).save(commit=False)
        link.starting_block = self.cleaned_data["starting_block"]
        link.ending_block = self.cleaned_data["ending_block"]
        link.creator = self.cleaned_data["creator"]
        link.warrant = self.cleaned_data['warrant']
        if commit:
            link.save()
        return link