from django.contrib import admin

# Register your models here.
from myapp.models import *

admin.site.register(Muni)
from guardian.admin import GuardedModelAdmin
from myapp.models import Disaster


class DAdmin(GuardedModelAdmin):
    pass

admin.site.register(Disaster,DAdmin)
