from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('mine_block',views.mine_block),
    path('getchain',views.getchain),
]
