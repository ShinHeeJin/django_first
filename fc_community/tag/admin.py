from django.contrib import admin

# Register your models here.

from .models import Tag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tag, TagAdmin)
