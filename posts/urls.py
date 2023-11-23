from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeViewSet, CommentViewSet
from .serializers import CommentSerializer

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
    path('likes/', LikeViewSet.as_view({'post': 'create'}), name='like-create'),
    path('comments/', CommentViewSet.as_view({'post': 'create'}), name='comment-create'),
]
