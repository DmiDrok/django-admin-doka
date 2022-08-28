from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Review, Order


class ReviewAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']
	list_display_links = ['id', 'name']


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'price', 'is_completed', 'date_create']
	list_display_links = ['id', 'name']
	list_editable = ['is_completed']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)