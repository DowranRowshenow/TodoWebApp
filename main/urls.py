from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('todos/', views.TodoListView.as_view(), name="todos"),
    path('language/<str:language_code>/', views.LanguageSwitchView.as_view(), name='language_switch'),
	path('todos/create_item/', views.CreateItemView.as_view(), name ='create_item'),
	path('todos/<pk>/edit_item/', views.EditItemView.as_view(), name ='edit_item'),
	path('todos/favorite_item/<int:item_id>/', views.FavoriteItemView.as_view(), name='favorite_item'),
	path('todos/complete_item/<int:item_id>/', views.CompleteItemView.as_view(), name='complete_item'),
	path('todos/recover_item/<int:item_id>/', views.RecoverItemView.as_view(), name='recover_item'),
    path('todos/<pk>/delete_item/', views.DeleteItemView.as_view(), name='delete_item'),
]