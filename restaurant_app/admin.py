from django.contrib import admin
from .models import Profile, Booking, Table, Status, Message, Notification
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.unregister(Group)
admin.site.register(Booking)
admin.site.register(Table)
admin.site.register(Status)
admin.site.register(Notification)

@admin.register(Message)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'email',)
	ordering = ('name',)
	search_fields = ('name', 'email')

class ProfileInline(admin.StackedInline):
	model=Profile

class UserAdmin(admin.ModelAdmin):
	model=User
	fields=('first_name', 'last_name', 'username', 'email',)
	list_display=('username', 'email',) 
	inlines=[ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)