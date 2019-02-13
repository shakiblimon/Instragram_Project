from django.urls import path, include

from posts.views import HomePageView, CreatePostView

urlpatterns = [
    path('home/', HomePageView.as_view(),name='home'),
    path('post/',CreatePostView.as_view(), name='add_post')

]
