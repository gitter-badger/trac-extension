# -*- encoding: utf-8 -*-
from django.shortcuts import render
from djtrac.models import Milestone, Ticket
from djtrac.forms import ReportForm

def main(request):
    form = ReportForm(request.GET)
    tickets = []
    if form.is_valid():
        milestone = form.cleaned_data.get('milestone')
        tickets = Ticket.objects.filter(milestone=milestone)
    else:
        pass
    c = {
        'milestones': Milestone.objects.all(),
        'form': form,
        'tickets': tickets
    }
    return render(request, 'index.html', c)

