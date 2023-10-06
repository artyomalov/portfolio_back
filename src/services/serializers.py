from rest_framework import serializers
from .models import ServiceModel


class ServiceModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    serviceTitle = serializers.CharField(max_length=512,
                                         source='service_title')
    servicePrice = serializers.CharField(max_length=100,
                                         source='service_price')
    serviceInfo = serializers.CharField(max_length=4000,
                                        source='service_info')

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
