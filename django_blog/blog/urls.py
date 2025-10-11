from django.urls import path
from . import views

urlpatterns = [
    # User authentication paths
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Blog post paths
    path('', views.PostListView.as_view(), name='post-list'),
    path('home/', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment paths
    path('post/<int:pk>/comments/new/',
         views.CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_pk>/comment/<int:pk>/update/',
         views.CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:post_pk>/comment/<int:pk>/delete/',
         views.CommentDeleteView.as_view(), name='comment-delete'),

]
