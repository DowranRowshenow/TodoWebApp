from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name="home"),
	path('home/favorites/', views.FavoritesView.as_view(), name='favorites'),
	path('home/deleted/', views.DeletedView.as_view(), name='deleted'),
	path('home/favorite_item/<item_id>/', views.FavoriteItemView.as_view(), name ='favorite_item'),
	path('home/complete_item/<item_id>/', views.CompleteItemView.as_view(), name='complete_item'),
	path('home/recover_item/<item_id>/', views.RecoverItemView.as_view(), name='recover_item'),
    path('home/delete_item/<item_id>/', views.DeleteItemView.as_view(), name='delete_item'),
]