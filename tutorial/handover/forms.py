from django import forms
from .models import CurrentHO
from bootstrap_datepicker_plus import DateTimePickerInput


class CurrentHOForm(forms.ModelForm):
        class Meta:
                model = CurrentHO
                fields = ('issue_type', 'updated_by', 'start_date', 'end_date', 'subject', 'status')
                widgets = {'issue_type':forms.Select(attrs={"class": "form-control"}),
                           'updated_by':forms.TextInput(attrs={"class": "form-control"}),
                           'start_date':DateTimePickerInput(),
                           'end_date':DateTimePickerInput(),
                           'subject':forms.Textarea(attrs={"class": "form-control"}),
                           'status':forms.Select(attrs={"class": "form-control"})}


"""
                Issue_Choices = (('Incident','Incident'),('Mail','Mail'),('Change','Change'))
                Status_Choices = (('Completed','Completed'),('Approved','Approved'),('Pending','Pending'),('Blocked','Blocked'))
                issue_type = forms.ChoiceField(choices=Issue_Choices, widget=forms.Select(attrs={"class": "form-control"}))
                updated_by = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class": "form-control"}))
                Start_Date = forms.DateTimeField(widget=DateTimePickerInput())
                End_Date = forms.DateTimeField(widget=DateTimePickerInput())
                Subject = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
                Status = forms.ChoiceField(choices=Status_Choices, widget=forms.Select(attrs={"class": "form-control"}))
"""








