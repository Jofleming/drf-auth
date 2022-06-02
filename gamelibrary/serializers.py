from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "name", "description", "created_at")
        model = Game
