from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, DetailView

from hamster.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'hamster/postlistview.html'
    paginate_by = 3


class PostDetailsView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'hamster/postdetailview.html'


def like_view(request, pk):
    user = request.user
    if not user.is_authenticated:
        raise PermissionDenied()
    post = get_object_or_404(Post, pk=pk)
    if user.liked_posts.filter(pk=post.pk):
        post.likes.remove(user)
    else:
        post.likes.add(user)
    post.save()
    return redirect(request.META.get('HTTP_REFERER'))



