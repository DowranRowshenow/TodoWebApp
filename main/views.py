from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import translation
from django.conf import settings
from django.http import HttpResponse
from main.models import Todo
from django.shortcuts import redirect

def redirect_to_base(request, exception):
    return redirect('/')

    
class LanguageSwitchView(View):
    def get(self, request, language_code):
        if language_code in [lang[0] for lang in settings.LANGUAGES]:
            translation.activate(language_code)
            response = HttpResponse(status=302)
            response['Location'] = request.META.get('HTTP_REFERER', '/')
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
            return response
        return redirect(request.META.get('HTTP_REFERER', '/'))


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
        is_favorite, is_complete, is_deleted = None, None, False
        if filterBy == 'favorites': is_favorite = True
        elif filterBy == '-favorites': is_favorite = False
        elif filterBy == 'completed': is_complete = True
        elif filterBy == '-completed': is_complete = False
        if pageBy == 'favorites': is_favorite = True
        elif pageBy == 'deleted': is_deleted = True
        if is_favorite: 
            if is_complete: queryset = Todo.objects.filter(owner = self.request.user, title__contains = searchBy, is_favorite = is_favorite, is_completed = is_complete, is_deleted = is_deleted).order_by(sortBy) 
            else: queryset = Todo.objects.filter(owner = self.request.user, title__contains = searchBy, is_favorite = is_favorite, is_deleted = is_deleted).order_by(sortBy)
        elif is_complete: queryset = Todo.objects.filter(owner = self.request.user, title__contains = searchBy, is_completed = is_complete, is_deleted = is_deleted).order_by(sortBy)
        else: queryset = Todo.objects.filter(owner = self.request.user, title__contains = searchBy, is_deleted = is_deleted).order_by(sortBy)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_string'] = '?page_by=' + str(self.request.GET.get("page_by", "home")) + '&search_by=' + str(self.request.GET.get("search_by", "")) + '&sort_by=' + str(self.request.GET.get("sort_by", "id")) + '&filter_by=' + str(self.request.GET.get("filter_by", "none")) + '&page='
        context['all_items_length'] = Todo.objects.filter(owner = self.request.user).count()
        return context


class CreateItemView(CreateView):
    model = Todo
    fields = ["title", "content", "target_date_time"]
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class EditItemView(UpdateView):
    model = Todo
    fields = ["title", "content", "target_date_time"]
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


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
        if item.is_deleted: item.is_deleted = False
        else: item.is_deleted = True
        item.save()
        return redirect(request.META.get('HTTP_REFERER'))


class DeleteItemView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todos')