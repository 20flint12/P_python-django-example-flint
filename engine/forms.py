
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
        fields = (
            'title', 'text', 'is_active', 'timezone', 'dst',
            'latitude', 'longitude',
        )

    # def __init__(self, *args, **kwargs):
    #     # TODO : move default values to FORM
    #     self.request = kwargs.pop('request', None)
    #     self.host = kwargs.pop('host', None)
    #     self.instance = kwargs.get('instance', None)
    #
    #     super(StudyModuleForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['name'].label = 'Module Name (Required)'
    #     self.fields['name'].widget.attrs.update({'required': True})
    #
    #     self.fields['description'].label = 'Module Description (Required)'
    #     self.fields['description'].required = True
    #     self.fields['description'].widget.attrs.update({'required': True})
    #
    #     self.fields['category'].label = 'Category (Optional)'
    #     self.fields['category'].required = False
    #
    #     self.fields['isbn'].label = 'Related ISBN (Optional)'
    #     self.fields['image'].label = 'Cover Image (Optional)'
    #
    #     for key in self.fields:
    #         self.fields[key].widget.attrs.update({'class': 'form-control'})
    #
    # def save(self, *args, **kwargs):
    #     return super(StudyModuleForm, self).save(*args, **kwargs)

