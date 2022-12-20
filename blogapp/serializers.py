from rest_framework import serializers


class BlogPostSirializer(serializers.Serializer):
    title = serializers.CharField()
    post_body = serializers.IntegerField()