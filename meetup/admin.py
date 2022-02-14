from django.contrib import admin
from .models import MeetUp, Location, Participant
# Register your models here.


class MeetUpAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'date', 'location',)
    list_filter = ('title','date', )


admin.site.register(MeetUp, MeetUpAdmin)
admin.site.register(Location)
admin.site.register(Participant)
