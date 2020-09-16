from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_page"),
    path('blog/', views.single, name="blog_page"),
]
