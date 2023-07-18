from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<int:pk>', views.PostDetailView.as_view(), name='detail_view'),
    path('add_post', views.PostCreateView.as_view(), name='add_post'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='update_post'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='delete_post'),

]