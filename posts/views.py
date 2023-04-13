from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
# from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class PostsList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialzer = PostSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serialzer.data)
