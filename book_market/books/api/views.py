from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book, Comment

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from books.api.permissions import IsAdminUserOrReadOnly


# concrete view
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]    


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        serializer.save(book=book)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUserOrReadOnly]


# class BookListCreateAPIView(ListModelMixin, CreateModelMixin,GenericAPIView):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()

#    listelemek
#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)

#    Oluşturabilmek
#    def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
