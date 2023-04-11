from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from . import views

app_name = 'blog'
router = SimpleRouter()
router.register('posts', views.PostView)

comment_router = NestedSimpleRouter(router, 'posts', lookup='post')
comment_router.register('comments', views.PostDetailView,
                        basename='comment-detail')

urlpatterns = router.urls + comment_router.urls
