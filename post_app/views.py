from django.shortcuts import render
from django.db.models import Q
from post_app.models import Posts
# PostSerializer : Post 모델을 직렬화, 역직렬화시 필요한 클래스
from post_app.serializers import PostSerializer
# api_view : DRF에서 HTTP메서드 (GET, POST, PUT, DELETE)를 처리하도록 뷰 정의
from rest_framework.decorators import api_view
# Response : DRF에서 제공하는 응답 객체로 json형식의 응답을 쉽게 반환처리
from rest_framework.response import Response
# status : HTTP통신 상태 코드를 제공하는 모듈, 성공이나 오류에 대한 상태 정보를 제공
from rest_framework import status

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'GET':
        posts = Posts.objects.all().order_by('-id')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def posts_detail(request, slug):
    try:
        post = Posts.objects.get(slug=slug)
    except Posts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(PostSerializer(post).data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def posts_search(request):
    query = request.query_params.get('search')
    posts = Posts.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(category__icontains=query))
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)