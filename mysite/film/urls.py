from django.urls import path,include
from . import views
from film.views import detail,listR
urlpatterns = [
 path('',views.indexx),
 path('/list',views.indexx),
 path('/listR',views.indexR,name="listeRealisa" ),
path('<int:myid>',detail),
 ]  