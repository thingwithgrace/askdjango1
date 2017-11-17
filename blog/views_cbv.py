from django import forms
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Post

''' 옵션 1
post_list = ListView.as_view(model=Post,
                             queryset=Post.objects.all().prefetch_related('tag_set', 'comment_set'),
                             paginate_by=10)
'''
''' 옵션 2 - 인자가 길어지거나 CBV 상 특정 멤버함수를 재정의하고 싶을 때(상속 활용) '''
class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().prefetch_related('tag_set', 'comment_set')
    paginate_by = 10

post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))