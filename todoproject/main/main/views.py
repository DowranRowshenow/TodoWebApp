from django.views.generic import View, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Todo

@login_required(login_url="/login")
def home_return(request):
    return redirect("/home/page_1")

class homeView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, page):
        limit = 10
        filtered_items = []
        sortBy = "id"
        filterBy = "none"
        filtered_items = home_filter(request, filterBy, sortBy)
        paginator = Paginator(filtered_items, limit)
        context = {
            'current_page': "home",
            'item_list': paginator.get_page(page),
            'num_pages': paginator.num_pages,
            'all_items_length': Todo.objects.filter(owner = request.user, is_deleted = False).count,
        }
        return render(request, 'home.html', context)
    def post(self, request, page):
        limit = 10
        filtered_items = []
        content = None
        target_date = None
        search_value = None
        sortBy = "id"
        filterBy = "none"
        try: content = request.POST['content']
        except: print('Content is not definied')
        try: target_date = request.POST['target_date']
        except: print('Target Date is not definied')
        try: search_value = request.POST['search_value']
        except: print('Search is not defined')
        try: sortBy = request.POST['sort_value']
        except: print('Sort is not definied')
        try: filterBy = request.POST['filter_value']
        except: print('Filter is not definied')
        if content:
            if target_date:
                Todo.objects.create(content = content, owner = request.user, target_date = target_date)
            else:
                Todo.objects.create(content = content, owner = request.user)
        if search_value:
            if filterBy == 'favorites':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_favorite = True, is_deleted = False).order_by(sortBy)
            elif filterBy == '-favorites':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_favorite = False, is_deleted = False).order_by(sortBy)
            elif filterBy == 'completed':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_completed = True, is_deleted = False).order_by(sortBy)
            elif filterBy == '-completed':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_completed = False, is_deleted = False).order_by(sortBy)
            else:
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_deleted = False).order_by(sortBy)
        else:
            filtered_items = home_filter(request, filterBy, sortBy)
        paginator = Paginator(filtered_items, limit)
        context = {
            'current_page': "home",
            'item_list': paginator.get_page(page),
            'num_pages': paginator.num_pages,
            'all_items_length': Todo.objects.filter(owner = request.user, is_deleted = False).count,
        }
        return render(request, 'home.html', context)

def home_filter(request, filterBy, sortBy):
    if filterBy == 'favorites':
        filtered_items = Todo.objects.filter(owner = request.user, is_favorite = True, is_deleted = False).order_by(sortBy)
    elif filterBy == '-favorites':
        filtered_items = Todo.objects.filter(owner = request.user, is_favorite = False, is_deleted = False).order_by(sortBy)
    elif filterBy == 'completed':
        filtered_items = Todo.objects.filter(owner = request.user, is_completed = True, is_deleted = False).order_by(sortBy)
    elif filterBy == '-completed':
        filtered_items = Todo.objects.filter(owner = request.user, is_completed = False, is_deleted = False).order_by(sortBy)
    else:
        filtered_items = Todo.objects.filter(owner = request.user, is_deleted = False).order_by(sortBy)
    return filtered_items

class favoritesView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, page):
        if request.user.is_anonymous:
            return redirect('/login')
        limit = 10
        filtered_items = []
        sortBy = "id"
        filterBy = "none"
        filtered_items = favorites_filter(request, filterBy, sortBy)
        paginator = Paginator(filtered_items, limit)
        context = {
            'current_page': "favorites",
            'item_list': paginator.get_page(page),
            'num_pages': paginator.num_pages,
            'all_items_length': Todo.objects.filter(owner = request.user, is_favorite = True, is_deleted = False).count,
        }
        return render(request, 'home.html', context)
    def post(self, request, page):
        limit = 10
        filtered_items = []
        content = None
        target_date = None
        search_value = None
        sortBy = "id"
        filterBy = "none"
        try: content = request.POST['content']
        except: print('Content is not definied')
        try: target_date = request.POST['target_date']
        except: print('Target Date is not definied')
        try: search_value = request.POST['search_value']
        except: print('Search is not defined')
        try: sortBy = request.POST['sort_value']
        except: print('Sort is not definied')
        try: filterBy = request.POST['filter_value']
        except: print('Filter is not definied')
        if content:
            if target_date:
                Todo.objects.create(content = content, owner = request.user, target_date = target_date)
            else:
                Todo.objects.create(content = content, owner = request.user)
        if search_value:
            if filterBy == 'favorites':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_favorite = True, is_deleted = False).order_by(sortBy)
            elif filterBy == '-favorites':
                filtered_items = []
            elif filterBy == 'completed':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_completed = True,is_favorite = True, is_deleted = False).order_by(sortBy)
            elif filterBy == '-completed':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_completed = False,is_favorite = True, is_deleted = False).order_by(sortBy)
            else:
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value,is_favorite = True, is_deleted = False).order_by(sortBy)
        else:
            filtered_items = favorites_filter(request, filterBy, sortBy)
        paginator = Paginator(filtered_items, limit)
        context = {
            'current_page': "favorites",
            'item_list': paginator.get_page(page),
            'num_pages': paginator.num_pages,
            'all_items_length': Todo.objects.filter(owner = request.user, is_favorite = True, is_deleted = False).count,
        }
        return render(request, 'home.html', context)

def favorites_filter(request, filterBy, sortBy):
    if filterBy == 'favorites':
        filtered_items = Todo.objects.filter(owner = request.user, is_favorite = True, is_deleted = False).order_by(sortBy)
    elif filterBy == '-favorites':
        filtered_items = []
    elif filterBy == 'completed':
        filtered_items = Todo.objects.filter(owner = request.user, is_completed = True,is_favorite = True, is_deleted = False).order_by(sortBy)
    elif filterBy == '-completed':
        filtered_items = Todo.objects.filter(owner = request.user, is_completed = False,is_favorite = True, is_deleted = False).order_by(sortBy)
    else:
        filtered_items = Todo.objects.filter(owner = request.user,is_favorite = True, is_deleted = False).order_by(sortBy)
    return filtered_items

class deletedView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, page):
        if request.user.is_anonymous:
            return redirect('/login')
        limit = 10
        filtered_items = []
        sortBy = "id"
        filterBy = "none"
        filtered_items = deleted_filter(request, filterBy, sortBy)
        paginator = Paginator(filtered_items, limit)
        context = {
            'current_page': "deleted",
            'item_list': paginator.get_page(page),
            'num_pages': paginator.num_pages,
            'all_items_length': Todo.objects.filter(owner = request.user, is_deleted = True).count,
        }
        return render(request, 'home.html', context)
    def post(self, request, page):
        limit = 10
        filtered_items = []
        content = None
        target_date = None
        search_value = None
        sortBy = "id"
        filterBy = "none"
        try: content = request.POST['content']
        except: print('Content is not definied')
        try: target_date = request.POST['target_date']
        except: print('Target Date is not definied')
        try: search_value = request.POST['search_value']
        except: print('Search is not defined')
        try: sortBy = request.POST['sort_value']
        except: print('Sort is not definied')
        try: filterBy = request.POST['filter_value']
        except: print('Filter is not definied')
        if content:
            if target_date:
                Todo.objects.create(content = content, owner = request.user, target_date = target_date)
            else:
                Todo.objects.create(content = content, owner = request.user)
        if search_value:
            if filterBy == 'favorites':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_favorite = True, is_deleted = False).order_by(sortBy)
            elif filterBy == '-favorites':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_favorite = False, is_deleted = True).order_by(sortBy)
            elif filterBy == 'completed':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_completed = True, is_deleted = True).order_by(sortBy)
            elif filterBy == '-completed':
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_completed = False, is_deleted = True).order_by(sortBy)
            else:
                filtered_items = Todo.objects.filter(owner = request.user, content__contains = search_value, is_deleted = True).order_by(sortBy)
        else:
            filtered_items = deleted_filter(request, filterBy, sortBy)
        paginator = Paginator(filtered_items, limit)
        context = {
            'current_page': "deleted",
            'item_list': paginator.get_page(page),
            'num_pages': paginator.num_pages,
            'all_items_length': Todo.objects.filter(owner = request.user, is_deleted = True).count,
        }
        return render(request, 'home.html', context)

def deleted_filter(request, filterBy, sortBy):
    if filterBy == 'favorites':
        filtered_items = Todo.objects.filter(owner = request.user, is_favorite = True, is_deleted = True).order_by(sortBy)
    elif filterBy == '-favorites':
        filtered_items = Todo.objects.filter(owner = request.user, is_favorite = False, is_deleted = True).order_by(sortBy)
    elif filterBy == 'completed':
        filtered_items = Todo.objects.filter(owner = request.user, is_completed = True, is_deleted = True).order_by(sortBy)
    elif filterBy == '-completed':
        filtered_items = Todo.objects.filter(owner = request.user, is_completed = False, is_deleted = True).order_by(sortBy)
    else:
        filtered_items = Todo.objects.filter(owner = request.user, is_deleted = True).order_by(sortBy)
    return filtered_items

class favoriteItemView(View):
    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        if (item.is_favorite):
            item.is_favorite = False
        else:
            item.is_favorite = True
        item.save()
        return redirect('/home/page_1')

class completeItemView(View):
    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        item.is_completed = not item.is_completed
        item.save()
        return redirect('/home/page_1')

class recoverItemView(View):
    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        item.is_deleted = False
        item.save()
        return redirect('/home/page_1')

class deleteItemView(View):
    def get(self, request, item_id):
        item = Todo.objects.filter(id = item_id).first()
        if (item.is_deleted):
            item.delete()
        else:
            item.is_deleted = True
            item.save()
        return redirect('/home/page_1')