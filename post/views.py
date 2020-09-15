from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Post, Category
from .serializers import PostSerializer

from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def blog_list(request, category):
  print(blog_list)
  if category == 'all':
    posts = Post.objects.all()
  else:
    posts = Post.objects.filter(category__text=category)
  serializer = PostSerializer(posts, many=True)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def blog_create(request):
  post = Post.objects.create(title=request.POST.get('title'), content=request.POST.get('content'), category=Category.objects.get(text=request.POST.get('category')), user=request.user)
  return Response(PostSerializer(post).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def blog_update(request):
  post = Post.objects.get(pk=request.POST.get('blog_id'))
  if post == None:
    return Response(status=status.HTTP_400_BAD_REQUEST)

  post.title = request.POST.get('title')
  post.content = request.POST.get('content')
  post.category = Category.objects.get(text=request.POST.get('category'))

  post.save()
  return Response(PostSerializer(post).data)

@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def blog_delete(request, blog_id):
  post = Post.objects.get(pk=blog_id)
  post.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def blog_detail(request, blog_id):
  post = Post.objects.get(pk=blog_id)
  return Response(PostSerializer(post).data)

@api_view(['GET'])
def auth_logout(request):
  logout(request)
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def auth_login(request):
  user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
  if user == None:
    return Response(status=status.HTTP_400_BAD_REQUEST)
  login(request, user)
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def auth_signup(request):
  user = User.objects.create_user(
    username = request.POST.get('email'),
    password = request.POST.get('password'),
    email = request.POST.get('email')
  )
  user.save( )

  return Response(status=status.HTTP_204_NO_CONTENT)