from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting_page'),
    path('posts', views.AllPostsView.as_view(), name='post_page'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post_detail_page'),
    path('read_later/', views.ReadLaterView.as_view(), name='read_later'),
]
