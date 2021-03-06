from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'goals'
urlpatterns = [

    # ex: /goals/
    path('', views.index, name='index'),
    # ex: /goals/1
    path('<int:goallist_id>', views.detail, name='detail'),
    # ex /goals/1/add/
    path('<int:goallist_id>/add/', views.add, name='add'),
    # ex /goals/completed
    path('<int:goallist_id>/completed/', views.completed, name='completed'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)