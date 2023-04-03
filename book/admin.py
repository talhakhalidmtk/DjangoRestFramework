from django.contrib import admin

from .models import Book, BookContributor

# Register your models here.
admin.site.register(Book)
admin.site.register(BookContributor)
