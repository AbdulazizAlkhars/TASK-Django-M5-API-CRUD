from django.contrib import admin

from .models import Booking, Flight

admin.site.register(Flight)
admin.site.register(Booking)


# class BookingAdmin(admin.ModelAdmin):
#     list_display = ("id", "date", "flight", "passenger")
#     list_filter = ("date",)
#     list_display_links = ("id", "date")
#     fieldsets = (
#         (None, {"fields": ("date", "flight", "passenger")}),
#     )
