from djoser.serializers import (UserCreateSerializer
                                as BaseUserRegistrationSerializer)
from djoser.serializers import UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
    Сериализатор для регистрации пользователей.

    Расширяет базовый сериализатор Djoser
     для регистрации, добавляя дополнительные поля.
    """

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('email', 'password', 'first_name',
                  'last_name', 'phone', 'avatar', 'town', 'role')


class UserSerializer(BaseUserSerializer):
    """
    Сериализатор для отображения информации о пользователе.

    Расширяет базовый сериализатор Djoser,
     включая дополнительные поля пользователя.
    """

    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'phone', 'avatar', 'town', 'role')
