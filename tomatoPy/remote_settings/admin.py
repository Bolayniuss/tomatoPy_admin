from django.contrib import admin

from json_field import JSONField
from splitjson import SplitJSONWidget

from .models import Setting
from .models import SettingValue


class SettingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': SplitJSONWidget}
    }


class SettingValueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Setting, SettingAdmin)
admin.site.register(SettingValue, SettingValueAdmin)
