from django.contrib import admin
from shop.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ItemComment(admin.StackedInline):
    model = Comments
    extra = 2


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')
    inlines = [ItemComment]


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)

