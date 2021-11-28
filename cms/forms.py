from django import forms

from cms.models import TasksModel


class CheckTaskForm(forms.Form):
    images = forms.ImageField(label='Изображения',
                              required=False,
                              widget=forms.ClearableFileInput(attrs={'class': 'form-control',
                                                                     'multiple': True}))

    def __init__(self, *args, **kwargs):
        checks = kwargs.pop('checks', 0)
        super(CheckTaskForm, self).__init__(*args, **kwargs)
        for check in checks:
            self.fields['extra_field_'+str(check.id)] = forms.BooleanField(label=check.name, required=False)



