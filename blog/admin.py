from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'date', 'tags')
    list_display = ('title', 'date', 'author')
    prepopulated_fields = {'slug': ('title',)}


class AdminComment(admin.ModelAdmin):
    list_display = ('user_name', 'post', 'text')
    list_filter = ('user_name', 'post')


admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment, AdminComment)
admin.site.register(Post, PostAdmin)
