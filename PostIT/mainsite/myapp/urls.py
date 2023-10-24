from django.urls import path
from django.urls import path
from django.contrib.auth.views import LogoutView
from .import views

urlpatterns = [
    path('', views.PostList.as_view(), name='posts_list'),
    path('create-posts/', views.create_posts, name='create-posts'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('my_posts/', views.MyPosts.as_view(), name='my_posts'),
    path('add-post/', views.PostCreate.as_view(), name='add_post'),
    path('post-update/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
    path('post-delete/<int:pk>/', views.DeleteView.as_view(), name='post_delete')
]