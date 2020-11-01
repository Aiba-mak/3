from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tweetapp.views import PostViewSet, CommentViewSet
from account.views import ProfileViewSet
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
schema_view = get_schema_view(title='Blog API')

router = DefaultRouter()
router.register('tweets', PostViewSet)
router.register('comment', CommentViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/account/', include('account.urls')),
    path('v1/', include('tweetapp.urls')),
    path('', include_docs_urls(title='Blog API')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
