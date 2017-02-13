from django.contrib import admin

# Register your models here.
from . import models

class BlogAdmin(admin.ModelAdmin):
	list_display = ['title', 'author']

	#self_filler = ['slug':('title',)]

admin.site.register(models.Blog, BlogAdmin)