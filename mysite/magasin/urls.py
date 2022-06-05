from django.urls import path,include
from . import views
from magasin.views import detail,checkout,confimation,listF

from magasin.views import listnameCateg
urlpatterns = [
 path('',views.index),
 path('/list',views.index),
path('/listF',views.indexF,name="listeFourniss" ),
 path('/listnameCateg',listnameCateg),
path('<int:myid>',detail),
 path('checkout', checkout),
  path('confirmation', confimation),
 ]