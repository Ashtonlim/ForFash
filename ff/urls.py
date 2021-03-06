from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cat_id>', views.cat, name='cat'),
    path('<int:cat_id>/<int:p_id>', views.product, name='product'),
]