from django.contrib import admin

# Register your models here.

from ppblog.models import Topic, Title, Entry

admin.site.register(Topic)
admin.site.register(Title)
admin.site.register(Entry)
