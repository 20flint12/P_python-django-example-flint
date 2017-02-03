
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
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
            'dtp1': forms.TextInput(attrs={"class": "form-control"}),

            'dtp2': forms.DateInput(attrs={'id': 'datetimepicker12'}),
            'dtp3': forms.DateTimeInput(attrs={'id': 'datetimepicker13'}),
        }

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs.update({'class': 'form-control'})

    def save(self, *args, **kwargs):
        return super(PlaceForm, self).save(*args, **kwargs)


class ToDoForm(forms.Form):

    # dp2 = forms.DateTimeField(
    #     required=False,
    #     widget=forms.DateInput(attrs={"class": "form-control",
    #                                   'id': 'datetimepicker14'}, )
    # )
    unaware_local = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"class": "form-control",
                                          'id': 'dtp_unaware_local',
                                          'size': '50', }, )
    )
    result = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control",
                                     'cols': 40, 'rows': 3}, )
    )
    '''
        <div class="input-group date" id="datetimepicker2">
            <input type="text" class="form-control">
            <span class="input-group-addon">
                <span class="glyphicon glyphicon-calendar"></span>
            </span>
        </div>

        <input class="form-control"
               id="datetimepicker15" name="unaware_local" type="text" required="">
    '''

# http://the7bits.com/blog/how-to-develop-custom-widget-in-django
