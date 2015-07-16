# -*- encoding: utf-8 -*-
from django import forms
from djtrac.models import Milestone

class ReportForm(forms.Form):
    milestone = forms.ChoiceField(
        choices=Milestone.objects.values_list('name', 'name')
    )