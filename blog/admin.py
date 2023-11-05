from django.contrib import admin
from .models import ItemMenu, Category


class ItemMenuAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('title', 'category')
    search_fields = ['title']


# Register your models here.

admin.site.register(ItemMenu, ItemMenuAdmin)
admin.site.register(Category)