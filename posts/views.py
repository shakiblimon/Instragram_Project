from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView

from posts.forms import PostForm
from posts.models import Post
from django.urls import reverse_lazy


class HomePageView(ListView):
     model = Post
     template_name = 'posts/home.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post.html'
    success_url = reverse_lazy('home')