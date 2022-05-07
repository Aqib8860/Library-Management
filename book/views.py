from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from django.core.exceptions import ObjectDoesNotExist
from book.serializers import BookSerializer, BorrowSerializer, ReturnSerializer
from user.models import User
from book.models import Book, Borrowed
from user.permissions import IsLibrarian, IsMember
from django.contrib.auth import get_user_model
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


User = get_user_model()


class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	#permission_classes = [permissions.IsAuthenticated, IsLibrarian]
	#filter_backends = [filters.SearchFilter]
	#search_fields = ['title', 'category']
	#http_method_names = ['get', 'post', 'options', 'head']


class ListBookViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class BorrowedViewSet(viewsets.ModelViewSet):
	queryset = Borrowed.objects.all()
	serializer_class = BorrowSerializer
	permission_classes = [permissions.IsAuthenticated, IsMember]
	http_method_names = ['get', 'post', 'options', 'head']

	def list(self, request, *args, **kwargs):
		try:
			user = User.objects.get(id=request.user.id)
		except ObjectDoesNotExist:
			return Response({"msg": "User Does not exist"}, status=400)

		queryset = self.queryset.filter(user_id=user)
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		# CHECK USER EXISTS
		try:
			user = User.objects.get(id=request.user.id)
		except ObjectDoesNotExist:
			return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

		# CHECK BOOK EXISTS
		try:
			book = Book.objects.get(id=request.data['book_id'])
		except ObjectDoesNotExist:
			return Response({"msg": "Book Does Not Exist"}, status=400)

		# CHECK BOOK ALREADY BORROWED
		if Book.objects.filter(id=request.data['book_id'], status="Borrowed").exists():
			return Response({"msg": "Book Already Borrowed"}, status=400)

		book = Book.objects.filter(id=request.data['book_id']).update(status="Borrowed")

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(
            serializer.save(user_id=request.user)
        )
		return Response({"msg": "Success"}, status=200)


class ReturnViewSet(viewsets.ModelViewSet):
	queryset = Borrowed.objects.all()
	serializer_class = ReturnSerializer
	#permission_classes = [permissions.IsAuthenticated, IsMember]
	http_method_names = ['patch', 'options', 'put']

	def perform_update(self, serializer):
		book = Book.objects.filter(id=self.request.data['book_id']).update(status="Available")
		serializer.save()

