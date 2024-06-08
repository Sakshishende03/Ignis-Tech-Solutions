from rest_framework import serializers

class CoinListSerializer(serializers.Serializer):
    coins = serializers.ListField(child=serializers.CharField())

class JobStatusSerializer(serializers.Serializer):
    job_id = serializers.UUIDField()
