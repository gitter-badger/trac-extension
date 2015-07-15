
from django.contrib import admin

from .models import Attachment, AuthCookie, Cache, Component, DjangoMigrations, Enum, Milestone, NodeChange,\
    Permission, Report, Repository, Revision, Session, SessionAttribute, System, Ticket, TicketChange, TicketCustom,\
    Version, Wiki

admin.site.register(Milestone)
admin.site.register(Ticket)
admin.site.register(TicketChange)