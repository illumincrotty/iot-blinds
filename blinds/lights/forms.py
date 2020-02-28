from django import forms


class DayForm(forms.Form):
    TIME_INPUT_FORMATS = ['%H:%M', '%I:%M%p', '%I:%M %p']

    start = forms.TimeField(label='Start Time', help_text='ex: 10:30AM', input_formats=TIME_INPUT_FORMATS)
    end = forms.TimeField(label='End Time', help_text='ex: 10:30AM', input_formats=TIME_INPUT_FORMATS)
    automatic = forms.BooleanField(label='Automatic', required=False)
