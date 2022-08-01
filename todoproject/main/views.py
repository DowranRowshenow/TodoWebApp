from django.views.generic import View, ListView
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, HttpResponseRedirect
from django.urls import reverse
from django.utils import translation
from main.models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'item_list'
    paginate_by = 10

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(TodoListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        pageBy = self.request.GET.get("page_by", "")
        searchBy = self.request.GET.get("search_by", "")
        sortBy = self.request.GET.get("sort_by", "id")
        filterBy = self.request.GET.get("filter_by", "none")
        is_favorite, is_complete = None, None
        if filterBy == 'favorites': is_favorite = True
        elif filterBy == '-favorites': is_favorite = False
        elif filterBy == 'completed': is_complete = True
        elif filterBy == '-completed': is_complete = False
        if pageBy == 'favorites':
            if is_complete: queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = True, is_completed = is_complete, is_deleted = False).order_by(sortBy)
            else: queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = True, is_deleted = False).order_by(sortBy)
            return queryset
        elif pageBy == 'deleted':
            if is_favorite: queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = is_favorite, is_deleted = True).order_by(sortBy)
            elif is_complete: queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_completed = is_complete, is_deleted = True).order_by(sortBy)
            else:  queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_deleted = True).order_by(sortBy)
            return queryset
        else:
            if is_favorite:  queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_favorite = is_favorite, is_deleted = False).order_by(sortBy)
            elif is_complete: queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_completed = is_complete, is_deleted = False).order_by(sortBy)
            else: queryset = Todo.objects.filter(owner = self.request.user, content__contains = searchBy, is_deleted = False).order_by(sortBy)
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = self.request.GET.get("page_by", "home")
        context['query_string'] = '?page_by=' + self.request.GET.get("page_by", "home") + '&search_by=' + str(self.request.GET.get("search_by", "")) + '&sort_by=' + str(self.request.GET.get("sort_by", "id")) + '&filter_by=' + str(self.request.GET.get("filter_by", "none")) + '&lang_by=' + str(self.request.GET.get("lang_by", "en")) + '&page='
        context['search_by'] = self.request.GET.get("search_by", "")
        context['sort_by'] = self.request.GET.get("sort_by", "id")
        context['filter_by'] = self.request.GET.get("filter_by", "none")
        context['lang_by'] = self.request.GET.get("lang_by", "en")
        context['is_favorites'] = self.request.GET.get("is_favorites", False)
        context['is_deleted'] = self.request.GET.get("is_deleted", False)
        context['all_items_length'] = Todo.objects.filter(owner = self.request.user, is_deleted = False).count()
        return context

    def get(self, request, *args, **kwargs):
        lang = self.request.GET.get("lang_by", "en")
        translation.activate(lang)
        return super().get(request, *args, **kwargs)

    def post(self, request):
        content = request.POST['content']
        target_date = request.POST['target_date']
        if content and target_date: Todo.objects.create(content = content, owner = request.user, target_date = target_date)
        return redirect(request.META.get('HTTP_REFERER'))


class FavoriteItemView(View):

    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        item.is_favorite = not item.is_favorite
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
        if item.owner == request.user:
            item.is_deleted = True
            item.save()
            if item.is_deleted: item.delete()
        return HttpResponseRedirect(reverse('todos'))