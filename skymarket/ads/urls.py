from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'ads/(?P<ad_pk>\d+)/comments',
                CommentViewSet, basename='ad-comments')

urlpatterns = [
    path('', include(router.urls)),
]
