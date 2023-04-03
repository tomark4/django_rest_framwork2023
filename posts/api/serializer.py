from rest_framework import serializers
from posts.models import Post
from django.utils.text import slugify
from random import randint
from users.api.serializer import UserSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  category = CategorySerializer()
  
  class Meta:
    model = Post
    fields = ['title','content','slug','thumbnail','published','user','category']


class PostCreateSerializer(serializers.ModelSerializer):
  slug = serializers.ReadOnlyField()
  
  class Meta:
    model = Post
    fields = ['title','slug','content','thumbnail','published','user','category']

  def create(self, validated_data):
    title = validated_data.get('title',None)
    slug = slugify(title)
    if Post.objects.filter(slug=slug).exists():
      extra = str(randint(1, 10000))
      slug = slugify(title) + "-" + extra 

    return Post.objects.create(**validated_data, slug=slug)