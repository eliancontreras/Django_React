from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.


class ProfilesList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serialzer = ProfileSerializer(profiles, many=True)
        return Response(serialzer.data)
