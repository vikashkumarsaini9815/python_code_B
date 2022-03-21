from django.contrib import admin
from .models import *
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display= ['id','headline','body_text','pub_date','mod_date','number_of_comments','number_of_pingbacks','rating']
    search_fields = ['headline',]
admin.site.register(Entry, EntryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display= ['id','name','tagline']
    search_fields = ['name',]
admin.site.register(Blog, BlogAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display= ['id','name','email']
    search_fields = ['name',]
admin.site.register(Author, AuthorAdmin)