from .models import Comment
from rest_framework import generics, permissions
from .serializers import CommentSerializer, CommentDetailSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CommentsList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Comment.objects.all()

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'post',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentDetailSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
