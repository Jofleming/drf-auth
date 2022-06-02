from rest_framework import generics
from .models import Game
from .permissions import IsOwnerOrReadOnly
from .serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer