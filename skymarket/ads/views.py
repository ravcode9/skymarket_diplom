from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import IsOwnerOrAdmin, IsAdminUser
from ads.serializers import AdSerializer, CommentSerializer


class AdCommentPagination(PageNumberPagination):
    """
    Пагинатор для объявлений и комментариев.

    Attributes:
        page_size (int): Количество объектов на странице.
    """
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с объявлениями.

    Поддерживает операции создания, чтения,
     обновления и удаления объявлений.
    Также включает фильтрацию, пагинацию
     и пользовательские разрешения.
    """

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter
    pagination_class = AdCommentPagination

    def perform_create(self, serializer):
        """
        Сохраняет автора объявления при его создании.

        Args:
            serializer: Сериализатор объявления.
        """
        serializer.save(author=self.request.user)

    def get_permissions(self):
        """
        Определяет разрешения в зависимости от действия.

        Returns:
            list: Список разрешений для текущего действия.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        elif self.action == 'get_my_ads':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'], url_path='me')
    def get_my_ads(self, request):
        """
        Возвращает объявления текущего пользователя.

        Args:
            request: HTTP запрос.

        Returns:
            Response: Ответ с сериализованными
             данными объявлений пользователя.
        """
        ads = self.get_queryset().filter(author=request.user)
        serializer = self.get_serializer(ads, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с комментариями.

    Поддерживает операции создания, чтения,
     обновления и удаления комментариев.
    Включает пользовательские разрешения
     и фильтрацию по объявлению.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Сохраняет автора комментария
         и связанное объявление при его создании.

        Args:
            serializer: Сериализатор комментария.
        """
        ad_id = self.kwargs.get('ad_pk')
        ad = Ad.objects.get(pk=ad_id)
        serializer.save(author=self.request.user, ad=ad)

    def get_queryset(self):
        """
        Возвращает queryset комментариев,
        отфильтрованный по объявлению, если указан ad_pk.

        Returns:
            QuerySet: Отфильтрованный queryset комментариев.
        """
        ad_id = self.kwargs.get('ad_pk')
        if ad_id:
            return self.queryset.filter(ad_id=ad_id)
        return self.queryset

    def get_permissions(self):
        """
        Определяет разрешения в зависимости от действия.

        Returns:
            list: Список разрешений для текущего действия.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        elif self.action in ['create']:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
