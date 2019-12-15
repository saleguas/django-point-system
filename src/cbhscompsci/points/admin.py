from django.contrib import admin
from .models import Student, MeetingKey, PointsEntry, CurrentKey
# Register your models here.

admin.site.site_header="Point System Administration"

class DisplayCodes(admin.ModelAdmin):
    list_display = ('name', 'qr_code')

admin.site.register(Student)
admin.site.register(MeetingKey, DisplayCodes)
admin.site.register(PointsEntry)
admin.site.register(CurrentKey)
