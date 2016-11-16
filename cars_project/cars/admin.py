from django.contrib import admin

from .models import User, Vehicle

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'phone_number',)


class VehicleAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'address', 'manufacturer', 'vehicle_number',)

	def name(self, instance):
		return instance.owners.username

	def phone(self, instance):
		return instance.owners.phone_number

	def address(self, instance):
		return instance.owners.address

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Vehicle, VehicleAdmin)

admin.site.site_title = 'My App Admin'
admin.site.site_header = "App Administrator"