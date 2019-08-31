from django.contrib import admin

from .models import Question, Rushee, RushComment

# Register your models here.
admin.site.register(Question)
admin.site.register(Rushee)
admin.site.register(RushComment)