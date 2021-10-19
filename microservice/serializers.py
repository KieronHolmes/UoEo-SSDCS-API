from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()


class ItemSerializer(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    authors = AuthorSerializer(many=True)


class ResultSerializer(serializers.Serializer):
    query = serializers.CharField()
    count = serializers.SerializerMethodField()
    results = ItemSerializer(many=True)

    def get_count(self, obj):
        return len(obj['results'])
