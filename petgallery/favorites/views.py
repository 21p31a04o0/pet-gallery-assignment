from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework.permissions import IsAuthenticated
from .models import Favorite
from .serializers import FavoriteSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
@api_view(['GET'])
def random_dog(request):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    image_url = data["message"]
    breed = image_url.split("/")[-2]

    return Response({
        "image_url": image_url,
        "breed": breed
    })
# Breed Dog Image
@api_view(['GET'])
def breed_dog(request, breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)
    data = response.json()
    return Response({
        "breed": breed,
        "image_url": data["message"]
    })