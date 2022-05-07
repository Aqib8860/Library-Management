from rest_framework import serializers
from book.models import Book, Borrowed


class BookSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = ['id', 'title', 'author', 'category', 'description', 'status']


class BorrowSerializer(serializers.ModelSerializer):
	user_id = serializers.ReadOnlyField(source='user.id')

	class Meta:
		model = Borrowed
		fields = '__all__'


class ReturnSerializer(serializers.ModelSerializer):
	book_id = serializers.SerializerMethodField()

	class Meta:
		model = Borrowed
		fields = ['book_id', 'returned']

	def get_book_id(self, obj):
		return self.obj.id