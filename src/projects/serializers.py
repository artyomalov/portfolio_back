from rest_framework import serializers


class PreviewModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    preview = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
    )
    alt_description = serializers.CharField(
        default='project preview',
        allow_null=False,
        max_length=200
    )


class ImageModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image_link = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
    )
    alt_description = serializers.CharField(
        default='project projects',
        allow_null=False,
        max_length=200
    )


class ProjectModelSerializerPreview(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=512)
    preview = serializers.SerializerMethodField(method_name='get_preview_url')

    def get_preview_url(self, obj):
        preview = obj.project_preview.preview
        domain = self.context.get('base_url')
        alt_description = obj.project_preview.alt_description
        return {
            'preview': (f'{domain}/media/{preview}'),
            'altDescription': alt_description
        }


class ProjectModelSerializerImages(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=512)
    description = serializers.CharField(max_length=4000)
    designerName = serializers.CharField(max_length=128,
                                         source='designer_name')
    images = serializers.SerializerMethodField(method_name='get_image_url')

    def get_image_url(self, obj):
        domain = self.context.get('base_url')
        images = obj.images.all()
        images_data = [
            {'id': image.id, 'imageUrl': f'{domain}/media/{image.image_link}',
             'altDescription': image.alt_description, } for image
            in
            images]
        return images_data
