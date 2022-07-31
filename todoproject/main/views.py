from django.views.generic import View, ListView
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.utils import translation
from main.models import Todo


class HomeView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'item_list'
    paginate_by = 10

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        searchBy = self.request.GET.get("search_by", "")
        sortBy = self.request.GET.get("sort_by", "id")
        filterBy = self.request.GET.get("filter_by", "none")
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
        context['query_string'] = '?search_by=' + str(self.request.GET.get("search_by", "")) + '&sort_by=' + str(self.request.GET.get("sort_by", "id")) + '&filter_by=' + str(self.request.GET.get("filter_by", "none")) + '&lang_by=' + str(self.request.GET.get("lang_by", "en")) + '&page='
        context['search_by'] = self.request.GET.get("search_by", "")
        context['sort_by'] = self.request.GET.get("sort_by", "id")
        context['filter_by'] = self.request.GET.get("filter_by", "none")
        context['lang_by'] = self.request.GET.get("lang_by", "en")
        context['all_items_length'] = Todo.objects.filter(owner = self.request.user, is_deleted = False).count()
        return context

    def get(self, request, *args, **kwargs):
        lang = self.request.GET.get("lang_by", "en")
        translation.activate(lang)
        return super().get(request, *args, **kwargs)

    def post(self, request):
        content = request.POST['content']
        target_date = request.POST['target_date']
        if content and target_date:
            Todo.objects.create(content = content, owner = request.user, target_date = target_date)
        return redirect(request.META.get('HTTP_REFERER'))


class FavoritesView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'item_list'
    paginate_by = 10

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(FavoritesView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        searchBy = self.request.GET.get("search_by", "")
        sortBy = self.request.GET.get("sort_by", "id")
        filterBy = self.request.GET.get("filter_by", "none")
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
        context['query_string'] = '?search_by=' + str(self.request.GET.get("search_by", "")) + '&sort_by=' + str(self.request.GET.get("sort_by", "id")) + '&filter_by=' + str(self.request.GET.get("filter_by", "none")) + '&lang_by=' + str(self.request.GET.get("lang_by", "en")) + '&page='
        context['search_by'] = self.request.GET.get("search_by", "")
        context['sort_by'] = self.request.GET.get("sort_by", "id")
        context['filter_by'] = self.request.GET.get("filter_by", "none")
        context['lang_by'] = self.request.GET.get("lang_by", "en")
        context['all_items_length'] = Todo.objects.filter(owner = self.request.user, is_deleted = False).count()
        return context

    def get(self, request, *args, **kwargs):
        lang = self.request.GET.get("lang_by", "en")
        translation.activate(lang)
        return super().get(request, *args, **kwargs)

    def post(self, request):
        content = request.POST['content']
        target_date = request.POST['target_date']
        if content and target_date:
            Todo.objects.create(content = content, owner = request.user, target_date = target_date)
        return redirect(request.META.get('HTTP_REFERER'))


class DeletedView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'item_list'
    paginate_by = 10

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(DeletedView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        searchBy = self.request.GET.get("search_by", "")
        sortBy = self.request.GET.get("sort_by", "id")
        filterBy = self.request.GET.get("filter_by", "none")
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
        context['query_string'] = '?search_by=' + str(self.request.GET.get("search_by", "")) + '&sort_by=' + str(self.request.GET.get("sort_by", "id")) + '&filter_by=' + str(self.request.GET.get("filter_by", "none")) + '&lang_by=' + str(self.request.GET.get("lang_by", "en")) + '&page='
        context['search_by'] = self.request.GET.get("search_by", "")
        context['sort_by'] = self.request.GET.get("sort_by", "id")
        context['filter_by'] = self.request.GET.get("filter_by", "none")
        context['lang_by'] = self.request.GET.get("lang_by", "en")
        context['all_items_length'] = Todo.objects.filter(owner = self.request.user, is_deleted = False).count()
        return context

    def get(self, request, *args, **kwargs):
        lang = self.request.GET.get("lang_by", "en")
        translation.activate(lang)
        translation.LANGUAGE_SESSION_KEY = lang
        return super().get(request, *args, **kwargs)

    def post(self, request):
        content = request.POST['content']
        target_date = request.POST['target_date']
        if content and target_date:
            Todo.objects.create(content = content, owner = request.user, target_date = target_date)
        return redirect(request.META.get('HTTP_REFERER'))


class FavoriteItemView(View):

    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        if (item.is_favorite):
            item.is_favorite = False
        else:
            item.is_favorite = True
        item.save()
        return redirect(request.META.get('HTTP_REFERER'))


class CompleteItemView(View):

    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        item.is_completed = not item.is_completed
        item.save()
        return redirect(request.META.get('HTTP_REFERER'))


class RecoverItemView(View):

    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        item.is_deleted = False
        item.save()
        return redirect(request.META.get('HTTP_REFERER'))


class DeleteItemView(View):

    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        if (item.is_deleted):
            item.delete()
        else:
            item.is_deleted = True
            item.save()
        return redirect('/home/?page=1')