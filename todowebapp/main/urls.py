from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home_return, name="home"),
    path('home/page_<page>', views.home, name="home"),
	path('home/favorite_item/<item_id>/', views.favorite_item, name ='favorite_item'),
	path('home/complete_item/<item_id>/', views.complete_item, name='complete_item'),
	path('home/recover_item/<item_id>/', views.recover_item, name='recover_item'),
    path('home/delete_item/<item_id>/', views.delete_item, name='delete_item'),
	path('home/favorites/page_<page>', views.favorites, name='favorites'),
	path('home/deleted/page_<page>', views.deleted, name='deleted'),
]