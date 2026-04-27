
from django.urls import path
from . import views
#localhost:8000/chai/  --> all chai page
#localhost:8000/chai/order --> green tea page
urlpatterns = [

    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),

]