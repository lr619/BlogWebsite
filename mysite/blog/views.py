from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
import markdown as md
# Create your views here.

class PostList(generic.ListView):
    queryset          =Post.objects.filter(status=1).order_by('-created_on')
    template_name     ='index.html'


class PostDetail(generic.DetailView):
    model              =Post
    template_name      ='post_detail.html'
'''
#attempt to use non template rendering to get python codeblocks to work
def detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    post.body=md.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, 'templates/post_detail.html', context={'post':post})'''