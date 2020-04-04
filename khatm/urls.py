from django.urls import path
from . import views

app_name = 'khatm'
urlpatterns = [
    path('', views.KhatmIndex.as_view() , name = 'khatm.joz'),
path('<int:khatm_id>/' , views.add_hezb , name = 'khatm.add'),
]
