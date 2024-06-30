from rest_framework.generics import GenericAPIView
from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book, Comment
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics

#concrete view
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    



# class BookListCreateAPIView(ListModelMixin, CreateModelMixin ,GenericAPIView):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()

#     #listelemek
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     #Oluşturabilmek
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    
