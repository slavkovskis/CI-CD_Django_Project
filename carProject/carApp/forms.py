from django import forms

from .models import Car


class CarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
    class Meta:
        model = Car
        fields = '__all__'