from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework import parsers, renderers, status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.post import Post
from ..models.hero import Hero
from .serializers import (CreateUserSerializer, AuthCustomTokenSerializer, UserSerializer, PostSerializer,
                          PostSearchSerializer, HeroSerializer)


class RegisterUserView(CreateAPIView):
    """
    User registration.
    """
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user.save()

        content = {
            'result': 'User created successfully',
        }

        return Response(content)


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        content = {
            'token': str(token.key),
        }

        return Response(content)


class PostList(ListCreateAPIView):
    """
    List all posts, or create a new post.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.filter(publish__lte=timezone.now()).order_by('publish')

    # def list(self, request, *args, **kwargs):
    #     posts = Post.objects.filter(publish__lte=timezone.now()).order_by('publish')
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.validated_data['post']
            post.author = request.user
            post.publish = timezone.now()
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostSearch(APIView):
    """
    Search post by text in title
    """
    permission_classes = ()
    serializer_class = PostSearchSerializer

    def post(self, request):
        serializer = PostSearchSerializer(data=request.data)
        serializer.is_valid()
        query = serializer.validated_data['query']
        posts = Post.objects. \
            filter(title__icontains=query). \
            filter(publish__lte=timezone.now()).\
            order_by('publish')

        serializerpost = PostSerializer(posts, many=True)
        return Response(serializerpost.data)


class UserProfile(RetrieveAPIView):
    """
    User profile.
    """
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        return user


class UserPosts(ListAPIView):
    """
    Posts published by user.
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        posts = Post.objects.filter(author__exact=user).order_by('publish')
        return posts


class Heroes(ListAPIView):
    """
    Hero published by user.
    """
    permission_classes = [AllowAny]
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()
