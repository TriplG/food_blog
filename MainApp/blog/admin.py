from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

#Подключаем в админку модели Article и Category
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)



