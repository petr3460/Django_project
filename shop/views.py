from django.shortcuts import render, redirect
from django.template import loader
from shop.models import Item, Category, Comments
from django.http import Http404
from .forms import CommentForm




def home(request):
    try:
        products = Item.objects.all()
        categories = Category.objects.all()
    except:
        raise Http404
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def item(request, alias):
    try:
        product = Item.objects.get(alias=alias)
        categories = Category.objects.all()
    except: raise Http404
    comment_form = CommentForm
    context = {
        'product': product,
        'categories': categories,
        'images': [product.image.url, ],
        'comments': Comments.objects.filter(comments_item_id=product.id),
        'form': comment_form
    }
    context.update(request)
    return render(request, 'item.html', context)


def get_category(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        products = Item.objects.filter(category=category)
        categories = Category.objects.all()
    except:
        raise Http404('Объекты не найдены')
    context = {
        'products': products,
        'category': category,
        'categories': categories,
    }
    return render(request, 'category.html', context)


def shipping(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
            }
    return render(request, 'shipping.html', context)


def about(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request, 'about.html', context)


def contacts(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'contacts.html', context)


def addcomment(request, alias):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_item = Item.objects.get(alias=alias)
            form.save()
    return redirect('/item/%s/' % alias)

