from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers
from . import views

app_name = 'blog'
router = routers.SimpleRouter()
router.register('posts', views.PostView)

comment_router = routers.NestedSimpleRouter(router, 'posts', lookup='post')
comment_router.register('comments', views.PostDetailView,
                        basename='comment-detail')

urlpatterns = router.urls + comment_router.urls
