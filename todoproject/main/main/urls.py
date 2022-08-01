from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home_return, name="home"),
    path('home/page_<page>', views.homeView.as_view(), name="home"),
	path('home/favorites/page_<page>', views.favoritesView.as_view(), name='favorites'),
	path('home/deleted/page_<page>', views.deletedView.as_view(), name='deleted'),
	path('home/favorite_item/<item_id>/', views.favoriteItemView.as_view(), name ='favorite_item'),
	path('home/complete_item/<item_id>/', views.completeItemView.as_view(), name='complete_item'),
	path('home/recover_item/<item_id>/', views.recoverItemView.as_view(), name='recover_item'),
    path('home/delete_item/<item_id>/', views.deleteItemView.as_view(), name='delete_item'),
]