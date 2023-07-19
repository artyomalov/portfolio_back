from rest_framework import serializers
from .models import ServiceModel


class ServiceModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service_title = serializers.CharField(max_length=512)
    service_price = serializers.CharField(max_length=100)
    service_info = serializers.CharField(max_length=4000)

    def create(self, validated_data: dict):
        return ServiceModel.objects.create(**validated_data)

    def update(self,
               instance: ServiceModel,
               validated_data: dict,
               ):
        instance.tab_title = validated_data.get('service_title',
                                                instance.service_title)
        instance.service_price = validated_data.get('service_price',
                                                    instance.service_price)
        instance.tab_info = validated_data.get('service_info',
                                               instance.service_title)
