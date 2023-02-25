from .views import DieselView
from django.urls import path

# for every URL created, it will add whatever was defined on the project level,
#which was defined as Diesel/
app_name = 'Diesel'
urlpatterns = [
    path('listing/',DieselView.as_view(),name='listing'),
    # path('submit/',save(),name='submit'),    
]