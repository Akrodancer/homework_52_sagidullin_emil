from django.urls import path
from to_do_list_app import views as to_do_list_app_views


urlpatterns = [
    path('', to_do_list_app_views.render_main_menu),
    path('index/', to_do_list_app_views.render_index),
    path('create/', to_do_list_app_views.create)
]