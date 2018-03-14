from django.shortcuts import render, redirect
from django.template import loader
from shop.models import Item, Category, Comments
from django.http import Http404
from .forms import CommentForm
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
import smtplib



def home(request):
    try:
        products = Item.objects.all()
        categories = Category.objects.all()
    except:
        raise Http404
    context = {
        'products': products,
        'categories': categories,
        'username': auth.get_user(request).username,
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
        'form': comment_form,
        'username': auth.get_user(request).username,
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
        'username': auth.get_user(request).username,
    }
    return render(request, 'category.html', context)


def shipping(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'username': auth.get_user(request).username,
            }
    return render(request, 'shipping.html', context)


def about(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'username': auth.get_user(request).username,
    }
    return render(request, 'about.html', context)


def contacts(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'username': auth.get_user(request).username,
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

def order(request, alias):
    if request.POST:
        name = request.POST['firstname']
        email = request.POST['email']
        content = 'name= '+ name + '\nemail is: ' + email + '\nproduct: ' + alias
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('tt1835935@gmail.com', 'Qazwsx122')
        mail.sendmail('fromdjango', 'petr3460@gmail.com', content)
        mail.close()
    return redirect('/item/%s/' % alias)


@csrf_protect
def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "user is not found"
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html', args)

@csrf_protect
def logout(request):
    auth.logout(request)
    return redirect('/')

@csrf_protect
def register(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', args)
