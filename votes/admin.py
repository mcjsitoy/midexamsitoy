from django.contrib import admin

# Register your models here.

from .models import Candidate, Position, Vote

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Position)
admin.site.register(Vote)
