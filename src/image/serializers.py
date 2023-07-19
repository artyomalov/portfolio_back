from rest_framework import serializers
from .models import ImageModel, PreviewModel
import os


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

    def create(self, validated_data):
        return ImageModel.objects.create(**validated_data)

    def update(self,
               instance: PreviewModel,
               validated_data: dict,
               ):
        instance.preview = validated_data.get(
            'preview',
            instance.preview
        )
        instance.alt_description = validated_data.get('alt_description',
                                                      instance.alt_description)
        return instance


class ImageModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image_link = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
    )
    alt_description = serializers.CharField(
        default='project image',
        allow_null=False,
        max_length=200
    )

    def create(self, validated_data):
        return ImageModel.objects.create(**validated_data)

    def update(self,
               instance: ImageModel,
               validated_data: dict,
               ):
        instance.image_link = validated_data.get(
            'image_link',
            instance.image_link
        )
        instance.alt_description = validated_data.get('alt_description',
                                                      instance.alt_description)
        return instance


class ProjectModelSerializerPreview(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=512)
    preview = serializers.SerializerMethodField(method_name='get_preview_url')

    def get_preview_url(self, obj):
        preview = obj.project_preview.preview
        domain = self.context.get('base_url')
        alt_description = obj.project_preview.alt_description
        print(f'{domain}/media/{preview}')
        return {
            'preview': (f'{domain}/media/{preview}'),
            'altDescription': alt_description
        }


class ProjectModelSerializerImages(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=512)
    description = serializers.CharField(max_length=4000)
    designer_name = serializers.CharField(max_length=128)
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


   #
   # old_preview = instance.image_link
   #      path_to_old_preview = os.path.join(
   #          os.path.abspath('.'),
   #          'media',
   #          'previews',
   #          str(old_preview).replace('/', '\\')
   #      )
   #      if path_to_old_preview is not None:
   #          if os.path.exists(path=path_to_old_preview):
   #              os.remove(path_to_old_preview)