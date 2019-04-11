from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)

#we added this outside of the tutorial to be able to alter the choices for the questions
admin.site.register(Choice)