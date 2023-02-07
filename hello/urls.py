from django.contrib import admin
from django.urls import path
from firstapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('edit/<int:id_>', views.edit),
    path('delete/<int:id_>', views.delete),

    path('admin/', admin.site.urls),
]
