from django.urls import path
from post.views import hola_mundo
urlpatterns=[

    path("",hola_mundo)

]