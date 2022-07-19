from django.views.generic import View, TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from main.models import Todo


class homeView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'item_list'
    paginate_by = 10

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(homeView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        searchBy = self.request.GET.get("search_value", "")
        sortBy = self.request.GET.get("sort_value", "id")
        filterBy = self.request.GET.get("filter_value", "none")
        if filterBy == 'favorites':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = True, is_deleted = False).order_by(sortBy)
        elif filterBy == '-favorites':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = False, is_deleted = False).order_by(sortBy)
        elif filterBy == 'completed':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_completed = True, is_deleted = False).order_by(sortBy)
        elif filterBy == '-completed':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_completed = False, is_deleted = False).order_by(sortBy)
        else:
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_deleted = False).order_by(sortBy)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'home'
        context['query_string'] = self.request.GET.copy().urlencode()
        context['all_items_length'] = Todo.objects.filter(owner = self.request.user, is_deleted = False).count()
        return context

    def post(self, request):
        content = request.POST['content']
        target_date = request.POST['target_date']
        Todo.objects.create(content = content, owner = request.user, target_date = target_date)
        return redirect(request.META.get('HTTP_REFERER'))


class favoritesView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'item_list'
    paginate_by = 10

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(favoritesView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        searchBy = self.request.GET.get("search_value", "")
        sortBy = self.request.GET.get("sort_value", "id")
        filterBy = self.request.GET.get("filter_value", "none")
        if filterBy == 'completed':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = True, is_completed = True, is_deleted = False).order_by(sortBy)
        elif filterBy == '-completed':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = True, is_completed = False, is_deleted = False).order_by(sortBy)
        else:
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = True, is_deleted = False).order_by(sortBy)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'favorites'
        context['query_string'] = self.request.GET.copy().urlencode()
        context['all_items_length'] = Todo.objects.filter(owner = self.request.user, is_deleted = False).count()
        return context

    def post(self, request):
        content = request.POST['content']
        target_date = request.POST['target_date']
        Todo.objects.create(content = content, owner = request.user, target_date = target_date)
        return redirect(request.META.get('HTTP_REFERER'))


class deletedView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'item_list'
    paginate_by = 10

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(deletedView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        searchBy = self.request.GET.get("search_value", "")
        sortBy = self.request.GET.get("sort_value", "id")
        filterBy = self.request.GET.get("filter_value", "none")
        if filterBy == 'favorites':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = True, is_deleted = True).order_by(sortBy)
        elif filterBy == '-favorites':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = False, is_deleted = True).order_by(sortBy)
        elif filterBy == 'completed':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_completed = True, is_deleted = True).order_by(sortBy)
        elif filterBy == '-completed':
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_completed = False, is_deleted = True).order_by(sortBy)
        else:
            queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_deleted = True).order_by(sortBy)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'deleted'
        context['query_string'] = self.request.GET.copy().urlencode()
        context['all_items_length'] = Todo.objects.filter(owner = self.request.user, is_deleted = False).count()
        return context

    def post(self, request):
        content = request.POST['content']
        target_date = request.POST['target_date']
        Todo.objects.create(content = content, owner = request.user, target_date = target_date)
        return redirect(request.META.get('HTTP_REFERER'))


class favoriteItemView(View):

    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        if (item.is_favorite):
            item.is_favorite = False
        else:
            item.is_favorite = True
        item.save()
        return redirect(request.META.get('HTTP_REFERER'))


class completeItemView(View):

    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        item.is_completed = not item.is_completed
        item.save()
        return redirect(request.META.get('HTTP_REFERER'))


class recoverItemView(View):

    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        item.is_deleted = False
        item.save()
        return redirect(request.META.get('HTTP_REFERER'))


class deleteItemView(View):

    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        if (item.is_deleted):
            item.delete()
        else:
            item.is_deleted = True
            item.save()
        return redirect('/home/?page=1')