from django.contrib import admin

# Register your models here.


from records.models import Publisher, Author, Book, RecNews

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)

admin.site.register(RecNews)