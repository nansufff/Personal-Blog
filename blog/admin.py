from django.contrib import admin
from .models import blogpost,tag,author
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter=("author","tags","date")
    list_display=("title","author","date")
    prepopulated_fields={"slug":("title",)}

admin.site.register(blogpost,PostAdmin)
admin.site.register(tag)
admin.site.register(author)