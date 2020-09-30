"""social_media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from tweetapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('tweetapp', include('tweetapp.urls')),
#     path('account', include('account.urls')),
# ]


from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from .yasg import urlpatterns as dic_url, schema_view
from rest_framework.routers import DefaultRouter

from tweetapp.views import PostViewSet, CommentViewSet
from account.views import ProfileViewSet
# from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
schema_view = get_schema_view(title='Blog API')

# API_TITLE = 'Blog API'
# API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
# schema_view = get_swagger_view(title=API_TITLE)

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('tweets', CommentViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/account/', include('account.urls')),
    # path('swagger-docs/', schema_view),
    path('v1/', include('tweetapp.urls')),
    path('docs/', include_docs_urls(title='Blog API')),
    path('schema/', schema_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += dic_url