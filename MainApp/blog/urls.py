from django.urls import path
from .views import *

#Указываем юрл адреса
urlpatterns = [
    path('', index, name='home'),
    path('rec/', add_rec, name='rec'),
    path('login/', LoginUser.as_view(), name='login'),
    path('registr/', RegisterUser.as_view(), name='registr'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('logout/', logout_user, name='logout'),
]

