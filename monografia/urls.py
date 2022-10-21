from django.contrib import admin
from django.urls import path
from monografia.views import home, formMonografias, formDiscentes, formCoAutores, buscarMonografias, formAutores, createmonografia, createcoautores, creatediscentes, createautores


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('formAutores/', formAutores),
    path('formCoAutores/', formCoAutores),
    path('formDiscentes/', formDiscentes),
    path('formMonografias/', formMonografias),
    path('createmonografia/', createmonografia),
    path('createcoautores/', createcoautores),
    path('creatediscentes/', creatediscentes),
    path('createautores/', createautores),
    path('buscarMonografia/',buscarMonografias ),

]