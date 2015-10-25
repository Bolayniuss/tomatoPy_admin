from django.core.exceptions import ObjectDoesNotExist
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.html import format_html

from django.conf import settings

from .models import TvShow
from accounts.models import Client


@admin.register(TvShow)
class TvShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'clients_column')

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    #def clients_column(self, model):
    #    return ", ".join(["{}".format(p) for p in model.client.select_related()])

    def clients_column(self, model):
        html = []
        for c in Client.objects.all():
            mode = "unused"
            if model.client.exists(id=c.id):
                mode = "used"
            html.append('<span style="color: {};"><b>{}</b></span>'.format(settings.ADMIN_RELATION_COLORS[mode], c.name))
        return format_html(", ".join(html))