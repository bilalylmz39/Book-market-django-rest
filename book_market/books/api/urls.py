from django.urls import path
from books.api import views as api_views

urlpatterns = [
    path('books/', api_views.BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', api_views.BookDetailAPIView.as_view(), name='book-details'),
    path('books/<int:book_id>/add_comment/', api_views.CommentCreateAPIView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', api_views.CommentDetailAPIView.as_view(), name='comment-details'),
]
