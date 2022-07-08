from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='index'),
    path('vinyls/<int:vinyl_id>/', views.vinyls_detail, name='detail'),
    # new route used to show a form and create vinyl
    path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
    path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
    path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
    path('vinyls/<int:vinyl_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('vinyls/<int:vinyl_id>/assoc_toy/<int:toy_id>/delete/', views.assoc_toy_delete, name='assoc_toy_delete'),
    path('vinyls/<int:vinyl_id>/add_playing/', views.add_playing, name='add_playing'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('vinyls/<int:vinyl_id>/add_photos/', views.add_photo, name='add_photo'),
    
    
]