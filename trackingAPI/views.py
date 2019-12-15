from django.shortcuts import render
from rest_framework import generics
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer
class ListCryptocurrencyView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer