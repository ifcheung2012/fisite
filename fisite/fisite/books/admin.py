
from django.contrib import admin
from fisite.books.models import  Publisher,Author,Book



class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email')
    search_field=('first_name','last_name')
    def save_model(self, request, obj, form, change):
        if getattr(obj,'added_by',None) is None:
            obj.added_by = request.user
        obj.added_by = request.user
        obj.save()

    def queryset(self, request):
            qs = super(AuthorAdmin, self).queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(added_by=request.user)

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


