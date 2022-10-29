from django.contrib import admin

from .models import Message, Room, Topic, User, Rating

# Register your models here.


admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Rating)
