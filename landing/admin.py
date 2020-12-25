from django.contrib import admin
from .models import *

class SubscriberAmin(admin.ModelAdmin):
    list_display =  [field.name for field in Subscriber._meta.fields]
    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAmin)