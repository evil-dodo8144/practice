
from django.urls import path
from . import views
# localhost:8000/dodoapp
urlpatterns = [
    path('',views.all_dodo,name='all_dodo'),

]
