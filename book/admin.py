from django.contrib import admin
from .models import Book, Borrowed

# Register your models here.


@admin.register(Borrowed)
class BorrowedAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'book_id', 'returned']
