from django import forms

class FilterForm(forms.Form):

    def __init__(self, choices, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['parameter_val'] = forms.MultipleChoiceField(choices=tuple([(f"{name[0]},{name[1]}", name[1]) for name in choices]), widget=forms.CheckboxSelectMultiple())

    class Meta:
        fields = ('parameter_val', )