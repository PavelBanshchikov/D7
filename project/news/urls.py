from django.urls import path
from .views import (PostList, PostDetail, PostCreate, PostDelete, PostUpdate, subscriptions)

urlpatterns = [path('', PostList.as_view(), name = 'post_list'),
               path('<int:pk>', PostDetail.as_view(), name='post_detail'),
               path('create/', PostCreate.as_view(), name='post_create'),
               path('<int:pk>/update/', PostUpdate.as_view(), name = 'post_update'),
               path('<int:pk>/delete/', PostDelete.as_view(), name = 'post_delete'),
               path('subscriptions/', subscriptions, name='subscriptions'),
               ]