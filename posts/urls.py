from django.urls import path, include
from .views import post_list, post_detail, post_create, post_edit, post_delete
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    # 템플릿용 경로
    path('', post_list, name='post_list'),  # /posts/로 접속 시 게시글 목록
    path('<int:pk>/', post_detail, name='post_detail'),  # /posts/1/ 상세페이지
    path('create/', post_create, name='post_create'),  # /posts/create/ 작성페이지
    path('<int:pk>/edit/', post_edit, name='post_edit'),  # /posts/1/edit/ 수정페이지
    path('<int:pk>/delete/', post_delete, name='post_delete'),  # /posts/1/delete/ 삭제

    # API 경로
    path('api/', include(router.urls)),
]
