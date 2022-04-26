from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# from .forms import LoginForm, UserRegistrationForm
from .forms import *
from .models import *

# Create your views here.
menu = [{'title': "Рецепты", 'url_name': 'home'},
        {'title': "Добавить рецепт", 'url_name': 'rec'},
        # {'title': "Зарегистрироваться", 'url_name': 'registr'},
        # {'title': "Войти", 'url_name': 'login'},
            ]

#Главная страница
def index(request):
    # menu = ["Главная страница", "Добавить статью", "Зарегистрироваться", "Войти"]

    articles = ["Все статьи", "Короновирус", "IT", "Футбол"]
    posts = Article.objects.all()
    cats = Category.objects.all()
    context = {
        'title': 'Рецепты',
        'cats': cats,
        'menu': menu,
        'articles': articles,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'blog/index.html', context=context)

#Доббавить рецепт
def add_rec(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    context = {
        'form': form,
        'title': 'Добавить рецепт',
        'menu': menu,
    }
    return render(request, 'blog/add.html', context=context)

#Регистрация
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/registr.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Регистрация'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'

        context['menu'] = menu
        return context
#Авторизация
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'blog/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'

        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             return render(request, 'blog/register_done.html', {'new_user': new_user, 'menu': menu})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'blog/registr.html', {'user_form': user_form, 'title': 'Регистрация', 'menu': menu})

#Отдельные статьи
def show_post(request, post_id):
    # return HttpResponse(f"Отображение статьи с id = {post_id}")
    posts = Article.objects.filter(id=post_id)
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Смотреть рецепт',
        'cat_selected': post_id,
        'cats': cats,
    }
    return render(request, 'blog/index.html', context=context)

#Выбор по категориям
def show_category(request, cat_id):
    posts = Article.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,

        'title': 'Выбор по категориям',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', context=context)
