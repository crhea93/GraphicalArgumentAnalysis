from django import forms
from .models import Block

class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = {
            'title',
            'num',
            'creator',
            'x_pos',
            'y_pos'
        }

    def save(self, commit=True):
        block = super(forms.ModelForm, self).save(commit=False)
        block.title = self.cleaned_data["title"]
        block.x_pos = self.cleaned_data["x_pos"]
        block.y_pos = self.cleaned_data["y_pos"]
        if commit:
            block.save()
        return block