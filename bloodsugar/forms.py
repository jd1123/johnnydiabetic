from django import forms
from bloodsugar.models import BloodSugarEntry

class BloodSugarEntryForm(forms.ModelForm):
    reading = forms.IntegerField()

    class Meta:
        model = BloodSugarEntry
        fields = ('reading',)
