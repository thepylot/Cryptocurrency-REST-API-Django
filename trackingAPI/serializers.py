from .models import Cryptocurrency
from rest_framework import serializers

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['cryptocurrency', 'price', 'market_cap', 'change']