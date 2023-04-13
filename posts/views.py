from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Post
from .serializers import PostSerializer
# from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class PostsList(APIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Post.objects.all()
        serialzer = PostSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serialzer.data)

    def post(self, request):
        serialzer = PostSerializer(
            data=request.data,
            context={'request': request}
        )
        if serialzer.is_valid():
            serialzer.save(owner=request.user)
            return Response(serialzer.data, status=status.HTTP_201_CREATED)

        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
