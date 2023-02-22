from rest_framework import serializers

class StockPriceSerializer(serializers.Serializer):
    current_price = serializers.IntegerField()