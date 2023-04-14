from .models import Like
from rest_framework import generics, permissions
from .serializers import LikeSerializer
from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class LikesList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    queryset = Like.objects.all()
