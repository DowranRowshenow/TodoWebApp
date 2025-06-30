from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from accounts import views
from django.conf.urls import handler404

handler404 = 'main.views.redirect_to_base'

def redirect_to_todos(request):
    return redirect('base')

urlpatterns = [
    path('', redirect_to_todos, name='main'),

    #path('', views.BaseView.as_view(), name="base"),
    path('admin/', admin.site.urls),
    # path('', include('main.urls')),
    # path('', include('accounts.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('', include('accounts.urls')),
)