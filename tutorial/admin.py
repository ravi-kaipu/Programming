from django.contrib import admin

from .models import AddMainTopic, AddSubTopic, Image

# Register your models here.

admin.site.register(AddMainTopic)
admin.site.register(AddSubTopic)
admin.site.register(Image)
