from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'update_date')
	ordering = ('title',)
	search_fields = ('title',)

#For a model to be accessible from the admin we have to register it
admin.site.register(Page, PageAdmin)

# Register your models here.
