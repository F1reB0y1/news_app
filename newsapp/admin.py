from django.contrib import admin
from .models import News, Author

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_of_publication')
    list_filter = ('author', 'date_of_publication')
    search_fields = ('title', 'full_text_of_material')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'bio')
    search_fields = ('name', 'surname')

admin.site.register(News, NewsAdmin)
admin.site.register(Author, AuthorAdmin)