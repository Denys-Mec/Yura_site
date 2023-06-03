from rest_framework import serializer
from .models import Author, Article

class ArticleSerializer(serializer.ModelSerializer):
    class Meta:
        model = Article
        fields = ['name', 'content',]
