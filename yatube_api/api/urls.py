from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/posts/<int:post_id>/comments/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
