from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.TodoListView.as_view(), name="todos"),
	path('todos/favorite_item/<item_id>/', views.FavoriteItemView.as_view(), name ='favorite_item'),
	path('todos/complete_item/<item_id>/', views.CompleteItemView.as_view(), name='complete_item'),
	path('todos/recover_item/<item_id>/', views.RecoverItemView.as_view(), name='recover_item'),
    path('todos/delete_item/<item_id>/', views.DeleteItemView.as_view(), name='delete_item'),
]