from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-me/', views.about_me, name='about-me'),
    path('add_posts/', views.add_posts, name='add_posts'),
    path('form_view/', views.form_view, name='form_view'),
    path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
    path('article/<int:id>/', views.article_detail, name='article'),
    path('article/delete/<int:article_id>/', views.delete_article, name='delete_article'),  # Corrected URL pattern
]
