from rest_framework.generics import GenericAPIView
from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book, Comment
from rest_framework.mixins import ListModelMixin, CreateModelMixin



class BookListCreateAPIView(ListModelMixin, CreateModelMixin ,GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
