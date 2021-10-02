from django.contrib import admin
from .models import Author, Book, BookInstance, Genre

admin.site.register(Genre)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birthday']
    fields = ['first_name', 'last_name', ('birthday', 'death')]


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']


class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
            (None, {'fields': ['book', 'imprint', 'language']}),
            ('Availability', {'fields': ['status', 'due_back']})
            )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
