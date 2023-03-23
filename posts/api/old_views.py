from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import (
HTTP_200_OK, 
HTTP_201_CREATED, 
HTTP_404_NOT_FOUND
)
from posts.models import Post
from .serializer import PostSerializer
from django.shortcuts import get_object_or_404

class PostViewSet(ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        
        return Response(status=HTTP_200_OK, data={
            'ok': True, 
            'message': 'success', 
            'posts': serializer.data
        })


    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=HTTP_201_CREATED, data=serializer.data)
    
    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        
        return Response(status=HTTP_200_OK, data={
            'message': 'success', 
            'post': serializer.data
        })


    # def retrieve(self, request, pk=None):
    #     try:
    #         post = Post.objects.get(id=pk)
    #         serializer = PostSerializer(post)
            
    #         return Response(status=HTTP_200_OK, data={
    #             'message': 'success', 
    #             'post': serializer.data
    #         })
    #     except Post.DoesNotExist: 
    #         return Response(status=HTTP_404_NOT_FOUND, data={
    #             'message': 'post not found', 
    #         })



# class PostApiView(APIView):
#     def get(self, request):
#         #posts = [post.title for post in Post.objects.all()]
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
        
#         return Response(status=HTTP_200_OK, data={
#             'ok': True, 
#             'message': 'success', 
#             'posts': serializer.data
#         })

#     def post(self, request):
#         # Post.objects.create(
#         #     title=request.data.get('title'),
#         #     description=request.data.get('description'),
#         #     order=request.data.get('order')
#         # )

#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(status=HTTP_201_CREATED, data=serializer.data)