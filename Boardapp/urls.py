from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:blog_id>',views.document_detail,name='document_detail'),


] 