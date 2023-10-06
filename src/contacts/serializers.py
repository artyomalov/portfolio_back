from rest_framework import serializers


class ContactModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=False, allow_null=False,
                                  max_length=50)
    content = serializers.CharField(allow_blank=False, allow_null=False,
                                    max_length=100)
    link = serializers.CharField(allow_blank=False, allow_null=False,
                                 max_length=200)
