from django.contrib import admin

# Register your models here.
from .models import info
from .models import CLUB
from .models import Review
from .models import Tag


admin.site.register(info)
admin.site.register(CLUB)
admin.site.register(Review)
admin.site.register(Tag)