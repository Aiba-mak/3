from django.urls import path

from . import views

urlpatterns = [
    # path('TagFilter/', views.TagFilter.as_view()),
    # path('PostViewSet/', views.PostViewSet.as_view()),
    # path('CommentViewSet/', views.CommentViewSet.as_view()),
    # path('TagViewSet/', views.TagViewSet.as_view()),
    path('FollowerList/', views.FollowerList.as_view()),
]




