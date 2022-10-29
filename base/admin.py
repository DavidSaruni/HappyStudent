from django.contrib import admin

from .models import Message, Room, Topic, User

# Register your models here.


admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
