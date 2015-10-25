from django.contrib import admin
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from django.utils.html import format_html

from .models import Movie, MovieRegistration
from accounts.models import Client


class MovieRegistrationInline(admin.TabularInline):
    model = MovieRegistration
    extra = 0
    fields = ('client', 'synchronized')
    #readonly_fields = ('client', )
    #formset = inlineformset_factory(Movie, MovieRegistration)
    #fields = ('__all__', )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'clients_column', )

    inlines = (
        MovieRegistrationInline,
    )

    def clients_column(self, model):
        html = []
        for c in Client.objects.all():
            mode = "unused"
            try:
                mr = model.movieregistration_set.get(client__id=c.id)
                if mr.synchronized:
                    mode = "sync"
                else:
                    mode = "used"
            except ObjectDoesNotExist:
                pass
            html.append('<span style="color: {};"><b>{}</b></span>'.format(settings.ADMIN_RELATION_COLORS[mode], c.name))
        return format_html(", ".join(html))



        #return ", ".join(["{}".format(p.client.name) for p in model.movieregistration_set.all()])

