from django.urls import path

from hamster.views import PostListView, PostDetailsView, like_view

app_name = "hamster"

urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailsView.as_view(), name='table'),
    path('like/<int:pk>/', like_view, name='like'),
]
