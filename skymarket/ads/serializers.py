from rest_framework import serializers
from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.

    Включает дополнительные поля для
     отображения информации об авторе и связанном объявлении.
    """

    author_first_name = serializers.CharField(
        source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(
        source='author.last_name', read_only=True)
    author_image = serializers.URLField(
        source='author.avatar', read_only=True)
    ad_id = serializers.IntegerField(
        source='ad.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['pk', 'text', 'author_id',
                  'created_at', 'author_first_name',
                  'author_last_name', 'ad_id', 'author_image']


class AdSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Ad.

    Включает дополнительные поля для
     отображения информации об авторе объявления.
    """

    author_first_name = serializers.CharField(
        source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(
        source='author.last_name', read_only=True)
    author_id = serializers.IntegerField(
        source='author.id', read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'title', 'price', 'image', 'description',
                  'author_first_name', 'author_last_name',
                  'author_id', 'created_at']
        read_only_fields = ['author', 'created_at']
