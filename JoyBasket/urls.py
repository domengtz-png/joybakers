
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name=home)
    path('contacts', views.contacts, name=contacts)
    path('about', views.about, name=about)
    path('payment', views.payment, name=payment)



]














