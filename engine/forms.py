
from django import forms

from engine.models import Place


class PlaceForm(forms.ModelForm):
    '''
    title = models.CharField(max_length=250)
    text = models.TextField()
    is_active = models.BooleanField(default=False)

    timezone = models.CharField(max_length=250, null=True, blank=True, default=None)     # "Europe/Zaporozhye"
    dst = models.BooleanField(blank=True, default=False)
    latitude = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(180.0)], null=True, blank=True, default=None)
    longitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], null=True, blank=True, default=None)
    '''

    class Meta:
        model = Place
        fields = '__all__'
        #     (
        #     # 'title', 'text', 'is_active', 'timezone', 'dst',
        #     # 'latitude', 'longitude',
        #     #
        #     # #'atodo', 'todata', 'reminder',
        # )

        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
            'dtp1': forms.TextInput(attrs={"class": "form-control"}),

            'dtp2': forms.DateInput(attrs={'id': 'datetimepicker12'}),
            'dtp3': forms.DateTimeInput(attrs={'id': 'datetimepicker13'}),
        }



        # def __init__(self, *args, **kwargs):
    #     super(PlaceForm, self).__init__(*args, **kwargs)
    #
    #     # self.fields['name'].label = 'Module Name (Required)'
    #     # self.fields['name'].widget.attrs.update({'required': True})
    #     #
    #     # self.fields['description'].label = 'Module Description (Required)'
    #     # self.fields['description'].required = True
    #     # self.fields['description'].widget.attrs.update({'required': True})
    #     #
    #     # self.fields['category'].label = 'Category (Optional)'
    #     # self.fields['category'].required = False
    #
    #     # self.fields['todo'].label = 'Related ISBN (Optional)'
    #     # self.fields['todo'] = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    #     # self.fields['image'].label = 'Cover Image (Optional)'
    #
    #     # for key in self.fields:
    #     #     self.fields[key].widget.attrs.update({'class': 'form-control'})

    # def save(self, *args, **kwargs):
    #     return super(StudyModuleForm, self).save(*args, **kwargs)


class ToDoForm(forms.Form):

    todo = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # date = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    # reminder = forms.DateTimeField(
    #     required=False, widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}))


