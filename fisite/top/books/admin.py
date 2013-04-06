
from django.contrib import admin
from fisite.books.models import  Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email')
    search_field=('first_name','last_name')
class BookAdmin(admin.ModelAdmin):
    list_display=('title','publisher','publication_date')
    list_filter=('publication_date',)
    #fields=('title','author','publisher')
    date_hierarchy='publication_date'
    ordering=('-publication_date',)
    raw_id_fields=('publisher',)

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)


