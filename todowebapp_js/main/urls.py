from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
	path('home/favorite_item/<item_id>/', views.favorite_item, name ='favorite_item'),
	path('home/complete_item/<item_id>/', views.complete_item, name='complete_item'),
	path('home/recover_item/<item_id>/', views.recover_item, name='recover_item'),
    path('home/delete_item/<item_id>/', views.delete_item, name='delete_item'),
	path('home/favorites/', views.favorites, name='favorites'),
	path('home/deleted/', views.deleted, name='deleted'),
]