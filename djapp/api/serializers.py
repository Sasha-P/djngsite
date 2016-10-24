from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model

from rest_framework import serializers

from ..models.post import Post
from ..models.hero import Hero


class CreateUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        User = get_user_model()

        if User.objects.filter(email=email).count():
            msg = _('User already exist.')
            raise ValidationError(msg)

        user = User(
            email=email,
            first_name=attrs['first_name'],
            last_name=attrs['last_name'],
        )

        user.set_password(password)

        attrs['user'] = user
        return attrs


class AuthCustomTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise ValidationError(msg)
        else:
            msg = _('Must include "email" and "password"')
            raise ValidationError(msg)

        attrs['user'] = user
        return attrs

    def validate_email(self, email):
        from django.core.validators import validate_email
        try:
            validate_email(email)
            return email
        except ValidationError:
            return False


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'date_joined', )


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'body', )

    def validate(self, attrs):
        post = Post(
            title=attrs['title'],
            text=attrs['body'],
        )

        attrs['post'] = post
        return attrs


class PostSearchSerializer(serializers.Serializer):
    query = serializers.CharField()


class HeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hero
        fields = ('id', 'name', )
