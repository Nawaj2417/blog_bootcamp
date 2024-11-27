# blog/serializers.py

from rest_framework import serializers
from .models import Blog,Category

# category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

        # blog 

class BlogSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    class Meta:
        model = Blog
        # fields = ['id', 'title', 'content', 'author', 'slug', 'category', 'image', 'created_at', 'updated_at']
        fields = '__all__'

